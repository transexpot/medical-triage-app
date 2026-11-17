import json
import os
import unittest


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

        # Имитируем перенос приёма на прошлую дату.
        past_appointment_date = "2026-10-01"

        # Проверяем, что новая дата в прошлом
        # относительно даты измерения глюкозы.
        self.assertLess(
            past_appointment_date,
            summary["glucose_measurement_date"],
        )

        # Проверяем, что данные полны:
        # все обязательные поля присутствуют.
        required_fields = [
            "summary_id",
            "patient_ref",
            "glucose_value",
            "glucose_unit",
            "glucose_condition",
            "glucose_measurement_date",
            "glucose_source",
        ]

        for field in required_fields:
            self.assertIn(field, summary)
            self.assertIsNotNone(summary[field])
            self.assertNotEqual(summary[field], "")

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.reschedule(summary, past_appointment_date)
        # и проверка:
        # self.assertEqual(result["status"], "DEADLINE_MISSED")
        # self.assertTrue(result["data_complete"])
        # self.assertIn("DEADLINE_MISSED", result["events"])


if __name__ == "__main__":
    unittest.main()
