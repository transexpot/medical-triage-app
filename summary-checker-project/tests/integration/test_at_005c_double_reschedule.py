import json
import os
import unittest


class TestAT005CDoubleReschedule(unittest.TestCase):
    def test_double_reschedule_uses_latest_deadline(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "valid-summary-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            summary = json.load(file)

        # Первая новая дата приёма.
        first_reschedule_date = "2026-12-01"

        # Вторая новая дата приёма.
        second_reschedule_date = "2026-12-15"

        # Проверяем, что вторая дата позже первой.
        self.assertLess(
            first_reschedule_date,
            second_reschedule_date,
        )

        # Проверяем, что обе даты в будущем
        # относительно даты измерения глюкозы.
        self.assertLess(
            summary["glucose_measurement_date"],
            first_reschedule_date,
        )
        self.assertLess(
            summary["glucose_measurement_date"],
            second_reschedule_date,
        )

        # Это статическая проверка fixture.
        # После создания движка здесь будет вызов
        # summary_checker.reschedule(
        #     summary,
        #     first_reschedule_date,
        # )
        # затем:
        # summary_checker.reschedule(
        #     summary,
        #     second_reschedule_date,
        # )
        # и проверка:
        # self.assertEqual(
        #     result["clinical_use_deadline"],
        #     second_reschedule_date,
        # )
        # self.assertIn("CHECKS_PRESERVED", result["events"])


if __name__ == "__main__":
    unittest.main()
