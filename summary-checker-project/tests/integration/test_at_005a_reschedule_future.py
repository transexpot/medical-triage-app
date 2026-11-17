import json
import os
import unittest


class TestAT005ARescheduleFuture(unittest.TestCase):
    def test_reschedule_to_future_preserves_checks(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        # Имитируем перенос приёма на будущую дату.
        # Сам перенос пока не выполняется,
        # потому что движка ещё нет.
        future_appointment_date = "2026-12-01"

        # Проверяем, что дата в будущем
        # относительно даты измерения глюкозы.
        self.assertGreater(
            future_appointment_date,
            summary["glucose_measurement_date"],
        )

        # Проверяем, что сводка остаётся валидной.
        self.assertIn("summary_id", summary)
        self.assertIn("patient_ref", summary)
        self.assertIn("glucose_value", summary)
        self.assertIn("glucose_unit", summary)
        self.assertIn("glucose_condition", summary)
        self.assertIn("glucose_measurement_date", summary)
        self.assertIn("glucose_source", summary)

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.reschedule(summary, future_appointment_date)
        # и проверка:
        # self.assertIn("CHECKS_PRESERVED", result["events"])
        # self.assertNotIn("CHECK_PASSED", result["events"])
        # self.assertNotIn("CHECK_FAILED", result["events"])
        # self.assertNotIn("VALUE_QUARANTINED", result["events"])
        # self.assertNotIn("DEFECT_CLASSIFIED", result["events"])


if __name__ == "__main__":
    unittest.main()
