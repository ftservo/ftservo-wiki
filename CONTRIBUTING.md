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

