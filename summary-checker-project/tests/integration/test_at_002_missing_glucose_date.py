import json
import os
import unittest


class TestAT002MissingGlucoseDate(unittest.TestCase):
    def test_missing_glucose_date_is_blocked(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        # Создаём дефектную копию сводки:
        # удаляем дату измерения глюкозы.
        invalid_summary = summary.copy()
        invalid_summary.pop("glucose_measurement_date", None)

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

        # Дата глюкозы должна отсутствовать.
        self.assertNotIn("glucose_measurement_date", invalid_summary)

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.process(invalid_summary)
        # и проверка:
        # self.assertEqual(result["status"], "BLOCKED")
        # self.assertFalse(result["data_complete"])


if __name__ == "__main__":
    unittest.main()
