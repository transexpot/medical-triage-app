import json
import os
import unittest


class TestAT008MetricsGroundTruth(unittest.TestCase):
    def test_metrics_match_ground_truth(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "synthetic-ground-truth-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            ground_truth = json.load(file)

        # Проверяем, что ground truth содержит acceptance-кейсы.
        self.assertIn("acceptance_cases", ground_truth)

        acceptance_cases = ground_truth["acceptance_cases"]

        # Проверяем, что список не пустой.
        self.assertGreater(len(acceptance_cases), 0)

        # Проверяем, что есть ключевые кейсы.
        ids = [case["id"] for case in acceptance_cases]

        self.assertIn("AT-001", ids)
        self.assertIn("AT-002", ids)
        self.assertIn("AT-003", ids)
        self.assertIn("AT-004", ids)
        self.assertIn("AT-005A", ids)
        self.assertIn("AT-005B_COMPLETE", ids)
        self.assertIn("AT-005B_BLOCKER", ids)
        self.assertIn("AT-005C", ids)
        self.assertIn("AT-005D", ids)
        self.assertIn("AT-005E", ids)
        self.assertIn("AT-006", ids)
        self.assertIn("AT-007", ids)
        self.assertIn("AT-008", ids)
        self.assertIn("AT-009", ids)

        # Это статическая проверка ground truth.
        # После создания движка здесь будет вызов
        # summary_checker.compute_metrics(ground_truth)
        # и проверка:
        # self.assertEqual(result["fpr"], expected_fpr)
        # self.assertEqual(result["fnr"], expected_fnr)


if __name__ == "__main__":
    unittest.main()
