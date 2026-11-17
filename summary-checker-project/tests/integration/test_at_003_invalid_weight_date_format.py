import json
import os
import unittest


class TestAT003InvalidWeightDateFormat(unittest.TestCase):
    def test_invalid_weight_date_format_is_warning(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        # Создаём копию валидной сводки
        # и подменяем дату веса на неверный формат.
        invalid_summary = summary.copy()
        invalid_summary["weight_measurement_date"] = "01.11.2026"

        # Дата веса должна присутствовать,
        # но иметь неверный формат.
        self.assertIn("weight_measurement_date", invalid_summary)
        self.assertEqual(
            invalid_summary["weight_measurement_date"],
            "01.11.2026",
        )

        # Обязательные поля глюкозы должны остаться корректными.
        self.assertIn("glucose_measurement_date", invalid_summary)
        self.assertIn("glucose_value", invalid_summary)
        self.assertIn("glucose_unit", invalid_summary)
        self.assertIn("glucose_condition", invalid_summary)
        self.assertIn("glucose_source", invalid_summary)

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.process(invalid_summary)
        # и проверка:
        # self.assertEqual(result["status"], "READY_WITH_WARNINGS")
        # self.assertTrue(result["data_complete"])


if __name__ == "__main__":
    unittest.main()
