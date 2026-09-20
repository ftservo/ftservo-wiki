"""Regression checks for package boundaries, bilingual drift and ZIP contents."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import product_package as package


class ProductPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.roots = (self.root / "zh", self.root / "en")
        self.id = "st-example-c001"
        self.manifest = package.new_manifest(self.id, "Example", "STS", "TTL")
        for en, root in enumerate(self.roots):
            folder = root / self.id
            package.write(folder / "manifest.json", json.dumps(self.manifest))
            package.write(folder / "main.md", "# Keep my specifications\n\n" + package.resource_section(self.manifest, bool(en)))
            package.write(folder / "software.md", "# Control\n")
            package.write(folder / "mechanical.md", "# Mechanics\n")
        self.override = patch.object(package, "MODEL_ROOTS", self.roots)
        self.override.start()
        self.addCleanup(self.override.stop)

    def test_missing_resource_is_valid_but_available_missing_file_fails(self):
        self.assertEqual(package.validate(), 1)
        item = self.manifest["assets"][0]
        item.update(status="available", path="datasheets/missing.pdf", source="Approved document")
        errors = package.validate_manifest(self.roots[0] / self.id, self.manifest)
        self.assertTrue(any("Missing or empty" in value for value in errors))

    def test_paths_cannot_escape_or_include_hidden_files(self):
        for path in ("../other/secret.txt", "C:/private.txt", "/private.txt", "images\\photo.png", ".env", "tests/.secret"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                package.asset_path(self.roots[0] / self.id, path)

    def test_bilingual_manifest_drift_is_rejected(self):
        path = self.roots[1] / self.id / "manifest.json"
        value = package.read_json(path)
        value["document_revision"] = "R2"
        package.write(path, json.dumps(value))
        with self.assertRaisesRegex(ValueError, "bilingual manifests differ"):
            package.validate()

    def test_refresh_preserves_specifications_and_repairs_only_resource_table(self):
        for root in self.roots:
            path = root / self.id / "main.md"
            package.write(path, path.read_text(encoding="utf-8").replace("| --- | --- | --- |", "| stale |"))
        with self.assertRaisesRegex(ValueError, "out of date"):
            package.validate()
        package.refresh()
        self.assertEqual(package.validate(), 1)
        for root in self.roots:
            self.assertTrue((root / self.id / "main.md").read_text(encoding="utf-8").startswith("# Keep my specifications"))

    def test_export_excludes_unlisted_drafts_and_checksums_match(self):
        for root in self.roots:
            package.write(root / self.id / "private-draft.txt", "Must not be exported")
        output = self.root / "bundle.zip"
        package.package(self.id, output)
        with zipfile.ZipFile(output) as archive:
            self.assertFalse(any("private-draft" in name for name in archive.namelist()))
            checksums = archive.read(f"{self.id}/SHA256SUMS.txt").decode().splitlines()
            self.assertEqual(len(checksums), 9)
            for record in checksums:
                digest, name = record.split("  ", 1)
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), digest)
        with self.assertRaisesRegex(ValueError, "overwrite"):
            package.package(self.id, output)

    def test_pwm_memory_table_is_not_applicable(self):
        manifest = package.new_manifest(self.id, "Example", "FT", "PWM")
        memory = next(item for item in manifest["assets"] if item["kind"] == "memory_table")
        self.assertEqual(memory["status"], "not_applicable")
        memory["status"] = "missing"
        self.assertTrue(any("PWM" in error for error in package.validate_manifest(self.roots[0] / self.id, manifest)))

    def test_same_filename_with_different_bilingual_contents_is_rejected(self):
        self.manifest["assets"][0].update(status="available", path="datasheets/revision.txt", source="Test fixture")
        for en, root in enumerate(self.roots):
            folder = root / self.id
            package.write(folder / "manifest.json", json.dumps(self.manifest))
            package.write(folder / "datasheets/revision.txt", f"Revision {en}")
        package.refresh()
        with self.assertRaisesRegex(ValueError, "bilingual asset bytes differ"):
            package.validate()

    def test_test_model_mismatch_is_rejected(self):
        folder = self.roots[0] / self.id
        item = next(a for a in self.manifest["assets"] if a["kind"] == "test_result")
        item.update(status="available", path="test-result.json", source="Test fixture", test_model="ExpectedModel")
        package.write(folder / "test-result.json", json.dumps({
            "model": "WrongModel", "measurements": [{"torque_nm": 1}],
            "range_profile": {"axes": {"torque_nm": {"min": 0, "max": 2}}},
        }))
        self.assertTrue(any("test_model" in error for error in package.validate_manifest(folder, self.manifest)))


if __name__ == "__main__":
    unittest.main()
