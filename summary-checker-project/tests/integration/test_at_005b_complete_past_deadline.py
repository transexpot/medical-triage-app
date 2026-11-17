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

from summary_checker.scheduler import reschedule


class TestAT005BCompletePastDeadline(unittest.TestCase):
    def test_past_deadline_with_complete_data(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        past_appointment_date = "2026-10-01"

        result = reschedule(
            summary,
            past_appointment_date,
        )

        self.assertEqual(
            result["status"],
            "DEADLINE_MISSED",
        )

        self.assertTrue(result["data_complete"])

        self.assertIn(
            "DEADLINE_MISSED",
            result["events"],
        )


if __name__ == "__main__":
    unittest.main()
