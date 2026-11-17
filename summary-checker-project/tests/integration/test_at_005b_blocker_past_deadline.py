import json
import os
import unittest


class TestAT005BBlockerPastDeadline(unittest.TestCase):
    def test_past_deadline_with_blocker(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        # Создаём копию сводки
        # и удаляем дату глюкозы,
        # чтобы получить BLOCKER.
        invalid_summary = summary.copy()
        invalid_summary.pop("glucose_measurement_date", None)

        # Имитируем перенос приёма на прошлую дату.
        past_appointment_date = "2026-10-01"

        # Проверяем, что дата в прошлом.
        self.assertLess(
            past_appointment_date,
            summary["glucose_measurement_date"],
        )

        # Проверяем, что блокер действительно есть:
        # дата глюкозы отсутствует.
        self.assertNotIn(
            "glucose_measurement_date",
            invalid_summary,
        )

        # Остальные обязательные поля должны остаться.
        required_fields = [
            "summary_id",
            "patient_ref",
            "glucose_value",
            "glucose_unit",
            "glucose_condition",
            "glucose_source",
        ]

        for field in required_fields:
            self.assertIn(field, invalid_summary)
            self.assertIsNotNone(invalid_summary[field])
            self.assertNotEqual(invalid_summary[field], "")

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.reschedule(
        #     invalid_summary,
        #     past_appointment_date,
        # )
        # и проверка:
        # self.assertEqual(result["status"], "BLOCKED")
        # self.assertFalse(result["data_complete"])
        # self.assertIn("DEADLINE_MISSED", result["events"])


if __name__ == "__main__":
    unittest.main()
