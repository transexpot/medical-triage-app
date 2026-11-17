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


class TestAT005ARescheduleFuture(unittest.TestCase):
    def test_reschedule_to_future_preserves_checks(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        future_appointment_date = "2026-12-01"

        result = reschedule(
            summary,
            future_appointment_date,
        )

        self.assertEqual(
            result["status"],
            "RESCHEDULED",
        )

        self.assertIn(
            "CHECKS_PRESERVED",
            result["events"],
        )

        self.assertIn(
            "APPOINTMENT_RESCHEDULED",
            result["events"],
        )

        self.assertNotIn(
            "CHECK_PASSED",
            result["events"],
        )

        self.assertNotIn(
            "CHECK_FAILED",
            result["events"],
        )

        self.assertNotIn(
            "VALUE_QUARANTINED",
            result["events"],
        )

        self.assertNotIn(
            "DEFECT_CLASSIFIED",
            result["events"],
        )


if __name__ == "__main__":
    unittest.main()
