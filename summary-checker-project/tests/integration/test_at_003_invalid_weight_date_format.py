import json
import os
import sys
import unittest


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "src",
        )
    ),
)

from summary_checker.engine import process


class TestAT003WarningOnly(unittest.TestCase):
    def test_warning_only_is_ready_with_warnings(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "warning-only-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        result = process(summary)

        self.assertEqual(
            result["status"],
            "READY_WITH_WARNINGS",
        )

        self.assertTrue(result["data_complete"])

        self.assertTrue(len(result["defects"]) > 0)

        self.assertIn(
            "INVALID_DATE_FORMAT",
            [defect["reason"] for defect in result["defects"]],
        )

        self.assertIn(
            "WARNING",
            [defect["class"] for defect in result["defects"]],
        )


if __name__ == "__main__":
    unittest.main()
