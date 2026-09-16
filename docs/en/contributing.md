# Wiki Maintenance

## Preview locally

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
cd ftservo-wiki
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`.

## Structure

- `docs/<path>.md`: Simplified Chinese.
- `docs/en/<same-path>.md`: English.
- `mkdocs.yml`: both navigation trees.
- `docs/assets/`: approved images, PDFs and small attachments.
- `sdk/`: official SDK submodules, not copied source trees.

Add Chinese and English together and add both navigation entries. Use lowercase English filenames with hyphens.

## Product-page checklist

1. Use the complete sales model.
2. Source parameters from an approved datasheet and record its revision/date.
3. Verify interface, voltage, pinout, dimensions, mass, speed, torque and travel.
4. Link the correct series and memory-table revision.
5. Use authorized, web-optimized media; never upload customer material.
6. Keep numbers, units and warnings identical across languages.
7. Obtain product-engineering and maintainer review.

## Add exact-model resources

1. Confirm the full sales model, document identifier and approved revision in `FTServos/型号.xlsx` and the PDF. Do not match filenames automatically; obtain product-engineering approval.
2. Create `docs/products/models/<lowercase-model>.md` and the matching English page under `docs/en/products/models/`. Record source, revision, rated conditions, interface, mounting, matching SDK and safety notes. Source each value from the exact-model PDF.
3. Add both pages to `mkdocs.yml`, link them from the [datasheet directory](products/datasheets/index.md), and cross-link drawings, curves and examples.
4. For performance curves, retain raw CSV data, test method and equipment details, then export a readable SVG/PNG. Identify voltage, ambient temperature, sample count, loading method, units and continuous-operation conditions. Distinguish measured points from fits and rated boundaries. Stall torque is not a continuous torque rating.
5. For CAD, publish STEP and a PDF mounting drawing with units, axes, zero position, holes, spline/horn, cable exit, revision and license. Mechanical engineering should compare dimensions with hardware and the datasheet.
6. Check matching values and warnings in both languages, run `mkdocs build --strict`, and request product, electrical/mechanical and Wiki-maintainer review.

See the [engineering resources page](resources/index.md) for the publication backlog and acceptance criteria.

## Submit and publish

```bash
git switch -c docs/model-name
git add docs mkdocs.yml
git commit -m "docs: add MODEL documentation"
git push -u origin HEAD
```

Open a pull request. A merge to `main` builds and deploys GitHub Pages. An administrator must first select **Settings → Pages → Source → GitHub Actions**. No domestic-server deployment is included.

Before submitting:

```bash
mkdocs build --strict
git diff --check
```

To update one reviewed/tested SDK pointer:

```bash
git submodule update --remote sdk/FTServo_Python
git add sdk/FTServo_Python
git commit -m "chore: update Python SDK"
```
