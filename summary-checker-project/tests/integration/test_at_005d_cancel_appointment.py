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

from summary_checker.scheduler import cancel_appointment


class TestAT005DCancelAppointment(unittest.TestCase):
    def test_cancel_appointment_archives_summary(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        result = cancel_appointment(summary)

        self.assertEqual(
            result["status"],
            "ARCHIVED",
        )

        self.assertTrue(result["data_complete"])

        self.assertIsNone(result["clinical_use_deadline"])

        self.assertIn(
            "APPOINTMENT_CANCELLED",
            result["events"],
        )

        self.assertIn(
            "CHECKS_PRESERVED",
            result["events"],
        )

        self.assertIn(
            "DEADLINE_CANCELLED",
            result["events"],
        )

        self.assertIn(
            "STATUS_COMPUTED",
            result["events"],
        )

        self.assertIn(
            "FLAG_COMPUTED",
            result["events"],
        )


if __name__ == "__main__":
    unittest.main()
