import json
import os
import unittest


class TestAT001ValidSummary(unittest.TestCase):
    def test_valid_summary_is_ready_for_physician(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

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

        self.assertEqual(summary["glucose_unit"], "mmol/L")
        self.assertEqual(summary["glucose_condition"], "FASTING")

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.process(summary)
        # и проверка:
        # self.assertEqual(result["status"], "READY_FOR_PHYSICIAN")
        # self.assertTrue(result["data_complete"])


if __name__ == "__main__":
    unittest.main()
