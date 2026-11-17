import json
import os
import unittest


class TestAT009Determinism(unittest.TestCase):
    def test_same_input_gives_same_result(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        # Проверяем, что сводка валидна.
        self.assertIn("summary_id", summary)
        self.assertIn("patient_ref", summary)
        self.assertIn("glucose_value", summary)
        self.assertIn("glucose_unit", summary)
        self.assertIn("glucose_condition", summary)
        self.assertIn("glucose_measurement_date", summary)
        self.assertIn("glucose_source", summary)

        # Это статическая проверка fixture.
        # После создания движка здесь будет два вызова
        # summary_checker.process(summary)
        # и проверка:
        # first_result = summary_checker.process(summary)
        # second_result = summary_checker.process(summary)
        # self.assertEqual(first_result, second_result)


if __name__ == "__main__":
    unittest.main()
