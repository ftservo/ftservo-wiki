"""人工确认参数的权威登记表（override 机制）。

背景：`import_official_servo_specs.py` 与 `import_models_buffer.py` 会用官网/缓冲区
数据回填或覆盖选型器数据 `docs/javascripts/servo-selector-data.js`，并重新生成型号页
`official-specs` 区块。工程师或厂家确认过的取值一旦与官方资料不一致，重跑导入就会
把人工结论冲掉、或让「待厂家确认」的警告重新出现。

本模块把这类人工确认记录在 `official_spec_overrides.json` 里，成为最终参数版本：
导入脚本每次运行都会读取它，命中的字段被强制写回，相关的自动冲突警告被抑制，
并改用登记表里的说明文案。值本身以 `fields` 为准，与官方原文的差异由 `notes` 说明，
官方逐字规格表行不做修改，保留追溯性。

用法（在导入脚本内）：

    import spec_overrides
    overrides = spec_overrides.load()
    override  = overrides.get(model.upper())
    spec_overrides.force(item, override)            # 强制人工确认值
    pending   = spec_overrides.suppress_notes(notes, override)   # 去掉已被确认取代的警告
    notes     = spec_overrides.confirmed_notes(override) + pending
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'scripts' / 'official_spec_overrides.json'

# 自动冲突警告的主题 -> 命中关键字（中/英各一份，用于定位要抑制的条目）
NOTE_TOPICS = {
    'case': ('外壳', 'Case:'),
    'motor': ('电机', 'Motor:'),
    'gear': ('齿轮', 'Gear'),
    'positionRange': ('位置控制范围', 'positionRange'),
    'voltageMin': ('输入电压下限', 'voltageMin'),
    'voltageMax': ('输入电压上限', 'voltageMax'),
}

# 选型器里受人工确认保护的分类字段（导入不应静默覆盖）
CLASSIFIED_KEYS = ('motor', 'motorNote', 'motorNoteEn', 'gear', 'case', 'shaft', 'continuous')


def load():
    """读取登记表，返回 {型号(大写): 条目}；文件不存在时返回空表。"""
    if not PATH.exists():
        return {}
    data = json.loads(PATH.read_text(encoding='utf-8'))
    return {str(key).upper(): value for key, value in (data.get('models') or {}).items()}


def fields(entry):
    """条目的强制字段；entry 为 None 时返回空字典。"""
    return dict((entry or {}).get('fields') or {})


def force(item, entry):
    """把人工确认值写到条目上（值为 None 表示删除该键）。"""
    for key, value in fields(entry).items():
        if value is None:
            item.pop(key, None)
        else:
            item[key] = value
    return item


def suppress_notes(notes, entry):
    """过滤掉已被人工确认值取代的自动冲突警告。"""
    keys = (entry or {}).get('suppress') or []
    if not keys:
        return list(notes)
    kept = []
    for note in notes:
        parts = note if isinstance(note, (list, tuple)) else [note]
        text = ' '.join(str(part) for part in parts)
        if any(token in text for key in keys for token in NOTE_TOPICS.get(key, ())):
            continue
        kept.append(note)
    return kept


def confirmed_notes(entry):
    """登记表里的说明文案，统一成 [中文, 英文] 形式。"""
    out = []
    for note in (entry or {}).get('notes') or []:
        if isinstance(note, dict):
            out.append([note.get('zh', ''), note.get('en', '')])
        else:
            out.append(list(note))
    return out
