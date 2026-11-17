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


class TestAT009Determinism(unittest.TestCase):
    def test_same_input_gives_same_result(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        first_result = process(summary)

        second_result = process(summary)

        self.assertEqual(
            first_result,
            second_result,
        )

        self.assertEqual(
            first_result["status"],
            "READY_FOR_PHYSICIAN",
        )

        self.assertTrue(first_result["data_complete"])


if __name__ == "__main__":
    unittest.main()
