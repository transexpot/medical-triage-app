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


class TestAT001ValidSummary(unittest.TestCase):
    def test_valid_summary_is_ready_for_physician(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        result = process(summary)

        self.assertEqual(
            result["status"],
            "READY_FOR_PHYSICIAN",
        )

        self.assertTrue(result["data_complete"])

        self.assertEqual(result["defects"], [])

        self.assertIn("STATUS_COMPUTED", result["events"])
        self.assertIn("FLAG_COMPUTED", result["events"])


if __name__ == "__main__":
    unittest.main()
