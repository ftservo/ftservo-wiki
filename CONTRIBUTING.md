# Maintaining FEETECH Wiki

## Documentation workflow

1. Create a branch such as `docs/sts3215`.
2. Add or update the Chinese page under `docs/`.
3. Make the equivalent English change at the same path under `docs/en/`.
4. If a page is new, add it to both language navigation trees in `mkdocs.yml`.
5. Verify every electrical value, dimension, register and unit against the
   exact model's approved datasheet and memory table.
6. Run `mkdocs build --strict` and `git diff --check`.
7. Open a pull request and request product-engineering review.

Do not commit confidential customer data, credentials, unlicensed media,
generated `site/` output, or unofficial software binaries.

## Confirmed parameters override imported data

`docs/javascripts/servo-selector-data.js` is the selector's source of truth and is
maintained by hand. The ingest scripts in `scripts/` re-fill it from crawled
manufacturer pages and from supplied model packages, which would otherwise
replace a value a human confirmed or bring back the "confirmation required"
warning that confirmation had resolved.

Record such values in `scripts/official_spec_overrides.json`:

```json
{
  "models": {
    "ST-3215-C001": {
      "fields": { "case": "plastic", "motor": "brushed-iron" },
      "suppress": ["case", "motor"],
      "notes": [{ "zh": "…", "en": "…" }]
    }
  }
}
```

- `fields` is written back on every run, so a confirmed value always wins over
  crawled or buffered data (`null` removes the key).
- `suppress` drops the automatic conflict warning for that topic and `notes`
  replaces it with the confirmed explanation; the block renders as `note` once
  nothing is left pending, and stays `warning` while other claims still need
  confirmation.
- The verbatim manufacturer specification table is never rewritten, so the
  source wording stays available for review.
- Shaft type (`single` / `dual`) is read from the product name first and only
  falls back to the introduction prose; inside one text a single-shaft wording
  wins over a dual-shaft one. Manufacturer introductions are occasionally copied
  between sibling models — ST-3036-C001 keeps 双轴 in its Chinese introduction
  while the same page reads 单轴 in the product name and Single-axis in English.

Both `import_official_servo_specs.py` and `import_models_buffer.py` read this file
through `scripts/spec_overrides.py`. Independently of the registry, neither script
overwrites `motor`, `gear`, `case`, `shaft` or `continuous` on a model that already
carries a value; newly supplied models are still populated in full.

Record only values a human confirmed. Do not copy script-derived values into the
registry.

## Ingest toolchain dependencies

The scripts that crawl, download or import official material need packages the
documentation build does not:

```bash
python -m pip install -r requirements-import.txt
```

`requirements.txt` stays limited to the MkDocs build and package validation that CI
runs.

## GitHub Pages

Repository administrators must select **Settings → Pages → Source → GitHub
Actions** once. A merge to `main` then runs `.github/workflows/pages.yml`. The
workflow only publishes GitHub Pages; it does not deploy to a domestic server.

## SDK submodules

Clone everything with:

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

Update one SDK only after reviewing and testing the upstream change:

```bash
git submodule update --remote sdk/FTServo_Python
git add sdk/FTServo_Python
git commit -m "chore: update Python SDK"
```

Rust SDK development is deferred until its support matrix, protocol tests and
hardware validation plan are approved.

