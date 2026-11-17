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


class TestAT005CDoubleReschedule(unittest.TestCase):
    def test_double_reschedule_uses_latest_deadline(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        first_reschedule_date = "2026-12-01"
        second_reschedule_date = "2026-12-15"

        first_result = reschedule(
            summary,
            first_reschedule_date,
        )

        second_result = reschedule(
            summary,
            second_reschedule_date,
        )

        self.assertEqual(
            first_result["status"],
            "RESCHEDULED",
        )

        self.assertEqual(
            second_result["status"],
            "RESCHEDULED",
        )

        self.assertEqual(
            second_result["clinical_use_deadline"],
            second_reschedule_date,
        )

        self.assertIn(
            "CHECKS_PRESERVED",
            second_result["events"],
        )

        self.assertIn(
            "APPOINTMENT_RESCHEDULED",
            second_result["events"],
        )


if __name__ == "__main__":
    unittest.main()
