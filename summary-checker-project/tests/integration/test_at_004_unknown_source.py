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


class TestAT004UnknownSource(unittest.TestCase):
    def test_unknown_source_needs_clarification(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "unknown-source-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        result = process(summary)

        self.assertEqual(
            result["status"],
            "NEEDS_CLARIFICATION",
        )

        self.assertFalse(result["data_complete"])

        source_defects = [
            defect
            for defect in result["defects"]
            if defect["field"] == "glucose_source"
        ]

        self.assertEqual(len(source_defects), 1)

        self.assertEqual(
            source_defects[0]["class"],
            "NEEDS_CLARIFICATION",
        )

        self.assertEqual(
            source_defects[0]["reason"],
            "UNKNOWN_SOURCE",
        )


if __name__ == "__main__":
    unittest.main()
