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


class TestAT004InvalidUnit(unittest.TestCase):
    def test_invalid_unit_is_blocked(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "invalid-unit-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        result = process(summary)

        self.assertEqual(
            result["status"],
            "BLOCKED",
        )

        self.assertFalse(result["data_complete"])

        self.assertTrue(len(result["defects"]) > 0)

        self.assertIn(
            "INVALID_UNIT",
            [defect["reason"] for defect in result["defects"]],
        )


if __name__ == "__main__":
    unittest.main()
