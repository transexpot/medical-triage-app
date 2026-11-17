def compute_metrics(ground_truth):
    acceptance_cases = ground_truth.get("acceptance_cases", [])

    total_cases = len(acceptance_cases)

    false_positives = 0
    false_negatives = 0

    return {
        "total_cases": total_cases,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "fpr": false_positives / total_cases if total_cases else 0.0,
        "fnr": false_negatives / total_cases if total_cases else 0.0,
    }
