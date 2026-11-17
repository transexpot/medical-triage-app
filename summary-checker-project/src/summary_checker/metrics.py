def compute_metrics(ground_truth):
    acceptance_cases = ground_truth.get("acceptance_cases", [])

    total_cases = len(acceptance_cases)

    false_positives = 0
    false_negatives = 0
    true_negatives = 0
    expected_positives = 0

    for case in acceptance_cases:
        expected_defect = False
        actual_defect = False

        if "expected_status" in case:
            expected_defect = case["expected_status"] != "READY_FOR_PHYSICIAN"
            actual_defect = case.get("actual_status") != "READY_FOR_PHYSICIAN"

        if "expected_data_complete" in case:
            if case["expected_data_complete"] is False:
                expected_defect = True

            if case.get("actual_data_complete") is False:
                actual_defect = True

        if "expected_event" in case:
            expected_defect = True
            actual_defect = case.get("actual_event") == case["expected_event"]

        if "expected_rule" in case:
            expected_defect = True
            actual_defect = case.get("actual_rule") == case["expected_rule"]

        if expected_defect:
            expected_positives += 1

            if not actual_defect:
                false_negatives += 1
        else:
            true_negatives += 1

            if actual_defect:
                false_positives += 1

    fpr_denominator = false_positives + true_negatives
    fnr_denominator = false_negatives + expected_positives

    return {
        "total_cases": total_cases,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "fpr": false_positives / fpr_denominator if fpr_denominator else 0.0,
        "fnr": false_negatives / fnr_denominator if fnr_denominator else 0.0,
    }
