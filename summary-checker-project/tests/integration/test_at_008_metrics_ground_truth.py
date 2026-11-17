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


if __name__ == "__main__":
    unittest.main()
