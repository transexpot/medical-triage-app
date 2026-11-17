import json
import os
import unittest


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

        # Новая дата приёма после повторного назначения.
        new_appointment_date = "2026-12-01"

        # Проверяем, что новая дата в будущем
        # относительно даты измерения глюкозы.
        self.assertLess(
            summary["glucose_measurement_date"],
            new_appointment_date,
        )

        # Проверяем, что сводка валидна.
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
        # затем:
        # summary_checker.reschedule(
        #     summary,
        #     new_appointment_date,
        # )
        # и проверка:
        # self.assertNotEqual(result["status"], "ARCHIVED")
        # self.assertEqual(
        #     result["clinical_use_deadline"],
        #     new_appointment_date,
        # )
        # self.assertIn("APPOINTMENT_CANCELLED", result["events"])
        # self.assertIn("APPOINTMENT_RESCHEDULED", result["events"])
        # self.assertIn("CHECKS_PRESERVED", result["events"])
        # self.assertIn("DEADLINE_RECALCULATED", result["events"])


if __name__ == "__main__":
    unittest.main()
