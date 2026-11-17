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

from summary_checker.scheduler import (
    cancel_appointment,
    reschedule,
)


class TestAT005ECancelAndReschedule(unittest.TestCase):
    def test_cancel_then_reschedule_dearchives_summary(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        new_appointment_date = "2026-12-01"

        cancel_result = cancel_appointment(summary)

        self.assertEqual(
            cancel_result["status"],
            "ARCHIVED",
        )

        self.assertIn(
            "APPOINTMENT_CANCELLED",
            cancel_result["events"],
        )

        reschedule_result = reschedule(
            summary,
            new_appointment_date,
        )

        self.assertNotEqual(
            reschedule_result["status"],
            "ARCHIVED",
        )

        self.assertEqual(
            reschedule_result["clinical_use_deadline"],
            new_appointment_date,
        )

        self.assertIn(
            "APPOINTMENT_RESCHEDULED",
            reschedule_result["events"],
        )

        self.assertIn(
            "CHECKS_PRESERVED",
            reschedule_result["events"],
        )

        self.assertIn(
            "DEADLINE_RECALCULATED",
            reschedule_result["events"],
        )


if __name__ == "__main__":
    unittest.main()
