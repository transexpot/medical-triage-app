import copy
import json
import os
import sys
import unittest


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "src",
        )
    ),
)

from summary_checker.metrics import compute_metrics


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

        result = compute_metrics(ground_truth)

        self.assertEqual(
            result["total_cases"],
            14,
        )

        self.assertEqual(
            result["false_positives"],
            0,
        )

        self.assertEqual(
            result["false_negatives"],
            0,
        )

        self.assertEqual(
            result["fpr"],
            0.0,
        )

        self.assertEqual(
            result["fnr"],
            0.0,
        )

    def test_metrics_detect_false_positive_and_false_negative(self):
        fixture_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fixtures",
            "synthetic-ground-truth-v1.json",
        )

        with open(fixture_path, "r", encoding="utf-8") as file:
            ground_truth = json.load(file)

        mutated_ground_truth = copy.deepcopy(ground_truth)

        false_positive_case = {
            "id": "AT-METRICS-FP",
            "expected_status": "READY_FOR_PHYSICIAN",
            "actual_status": "BLOCKED",
        }

        false_negative_case = {
            "id": "AT-METRICS-FN",
            "expected_status": "BLOCKED",
            "actual_status": "READY_FOR_PHYSICIAN",
        }

        mutated_ground_truth["acceptance_cases"].append(
            false_positive_case
        )

        mutated_ground_truth["acceptance_cases"].append(
            false_negative_case
        )

        result = compute_metrics(mutated_ground_truth)

        self.assertEqual(
            result["total_cases"],
            16,
        )

        self.assertEqual(
            result["false_positives"],
            1,
        )

        self.assertEqual(
            result["false_negatives"],
            1,
        )

        self.assertEqual(
            result["fpr"],
            1 / 15,
        )

        self.assertEqual(
            result["fnr"],
            1 / 1,
        )


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
