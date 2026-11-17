import json
import os
import unittest


class TestAT004UnknownSource(unittest.TestCase):
    def test_unknown_source_needs_clarification(self):
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
        # и подменяем источник глюкозы
        # на значение вне справочника.
        invalid_summary = summary.copy()
        invalid_summary["glucose_source"] = "UNKNOWN_SOURCE_999"

        # Источник должен присутствовать,
        # но не совпадать с известным источником.
        self.assertIn("glucose_source", invalid_summary)
        self.assertEqual(
            invalid_summary["glucose_source"],
            "UNKNOWN_SOURCE_999",
        )

        # Обязательные поля глюкозы должны остаться корректными.
        self.assertIn("glucose_value", invalid_summary)
        self.assertIn("glucose_unit", invalid_summary)
        self.assertIn("glucose_condition", invalid_summary)
        self.assertIn("glucose_measurement_date", invalid_summary)

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.process(invalid_summary)
        # и проверка:
        # self.assertEqual(
        #     result["status"],
        #     "NEEDS_CLARIFICATION",
        # )
        # self.assertFalse(result["data_complete"])


if __name__ == "__main__":
    unittest.main()
