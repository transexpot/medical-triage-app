import json
import os
import unittest


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

        # Проверяем, что сводка валидна до отмены.
        self.assertIn("summary_id", summary)
        self.assertIn("patient_ref", summary)
        self.assertIn("glucose_value", summary)
        self.assertIn("glucose_unit", summary)
        self.assertIn("glucose_condition", summary)
        self.assertIn("glucose_measurement_date", summary)
        self.assertIn("glucose_source", summary)

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.cancel_appointment(summary)
        # и проверка:
        # self.assertEqual(result["status"], "ARCHIVED")
        # self.assertIn("APPOINTMENT_CANCELLED", result["events"])
        # self.assertIn("CHECKS_PRESERVED", result["events"])
        # self.assertIn("DEADLINE_CANCELLED", result["events"])
        # self.assertIn("STATUS_COMPUTED", result["events"])
        # self.assertIn("FLAG_COMPUTED", result["events"])


if __name__ == "__main__":
    unittest.main()
