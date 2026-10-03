"""Validate selector data and refresh bilingual catalog cards from that data."""
import json
import math
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'docs/javascripts/servo-selector-data.js'


def load_data():
    return json.loads(DATA.read_text(encoding='utf-8').split('=', 1)[1].strip().rstrip(';'))


def validate(items):
    ids = set()
    for item in items:
        assert item['model'] not in ids, 'Duplicate model'
        ids.add(item['model'])
        for key in ('torque', 'speed', 'speedVoltage', 'positionRange', 'weight', 'weightTolerance', 'voltageMin', 'voltageMax'):
            value = item.get(key)
            assert value is None or (type(value) in (int, float) and math.isfinite(value) and value >= 0), (item['model'], key)
        assert item.get('continuous') is None or type(item['continuous']) is bool, (item['model'], 'continuous')
        dimensions = item.get('dimensions')
        assert dimensions is None or (isinstance(dimensions, list) and len(dimensions) == 3 and all(type(v) in (int, float) and math.isfinite(v) and v > 0 for v in dimensions))
        for key, values in {'motor': ['brushed-iron', 'brushed-coreless', 'brushless-coreless'], 'gear': ['copper', 'steel', 'titanium', 'plastic'], 'case': ['plastic', 'metal', 'hybrid'], 'shaft': ['single', 'dual']}.items():
            assert item.get(key) is None or item[key] in values, (item['model'], key)
        for image in [item.get('image'), item.get('drawing')]:
            if image:
                assert (ROOT / 'docs/products' / image).is_file(), image
                assert (ROOT / 'docs/en/products' / image).is_file(), image


def sync():
    items = load_data()
    validate(items)
    by_id = {i['model'].lower(): i for i in items}
    for locale in ('', 'en/'):
        for page in (ROOT / f'docs/{locale}products/datasheets').glob('*.md'):
            text = page.read_text(encoding='utf-8')
            def update(match):
                card = match[0]
                model = re.search(r'models/([^/]+)/main/', card)
                if not model or model[1] not in by_id:
                    return card
                item = by_id[model[1]]
                card = re.sub(r'\s*<figure class="ft-product-image">.*?</figure>', '', card, flags=re.S)
                image = item.get('image') or 'models/hl-3950-c001/images/main.webp'
                placeholder = not item.get('image')
                caption = ('Placeholder · HL-3950-C001' if locale else '占位图 · HL-3950-C001') if placeholder else ''
                figure = f'\n  <figure class="ft-product-image"><img src="../../{escape(image)}" alt="{escape(caption or item["model"])}" loading="lazy" width="800" height="800"><figcaption>{caption}</figcaption></figure>'
                metrics = []
                for key, zh, en, unit in [('voltage', '输入电压', 'Input voltage', 'V'), ('torque', '堵转扭矩', 'Stall torque', 'kg·cm'), ('speed', '空载速度', 'No-load speed', 'rpm')]:
                    value = item.get(key)
                    display = item.get(key + 'Label') or f'{value} {unit}' if value is not None else ('Not provided' if locale else '待补充')
                    metrics.append(f'<div><dt>{en if locale else zh}</dt><dd>{escape(display)}</dd></div>')
                card = re.sub(r'<dl class="ft-selector-metrics">.*?</dl>', '<dl class="ft-selector-metrics">' + ''.join(metrics) + '</dl>', card, flags=re.S)
                return card.replace('>','>' + figure, 1)
            updated = re.sub(r'<article class="ft-selector-card servo-catalog-card">.*?</article>', update, text, flags=re.S)
            if updated != text:
                page.write_text(updated, encoding='utf-8')
    print(f'Validated {len(items)} models; refreshed bilingual catalog images.')


if __name__ == '__main__':
    sync()
