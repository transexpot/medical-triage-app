            actual_defect = case.get("actual_rule") == case["expected_rule"]

        if not expected_defect and actual_defect:
            false_positives += 1
            false_negatives += 1

        if expected_defect and not actual_defect:
            false_negatives += 1
            false_positives += 1

    return {
        "total_cases": total_cases,
