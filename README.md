# FEETECH Wiki

Official bilingual documentation and developer resources for FEETECH servos.

- Website: <https://ftservo.github.io/ftservo-wiki/>
- Product website: <https://www.feetechrc.com/>
- SDK organization: <https://github.com/ftservo>

## Local preview

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000/>. The documentation source is under `docs/`;
Simplified Chinese is the default and English lives under `docs/en/`.

## Get the documentation and SDKs

The official SDK repositories are attached as Git submodules under `sdk/`.

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

If the repository was cloned without submodules:

```bash
git submodule update --init --recursive
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the maintenance workflow.
