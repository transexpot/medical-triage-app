import json
from datetime import datetime


REQUIRED_FIELDS = [
    "summary_id",
    "patient_ref",
    "glucose_value",
    "glucose_unit",
    "glucose_condition",
    "glucose_measurement_date",
    "glucose_source",
]

VALID_UNITS = {
    "mmol/L",
    "mg/dL",
    "%",
    "kg",
}

VALID_CONDITIONS = {
    "FASTING",
    "POSTPRANDIAL",
    "RANDOM",
}


def is_valid_iso_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (TypeError, ValueError):
        return False


def validate_summary(summary):
    result = {
        "status": "READY_FOR_PHYSICIAN",
        "data_complete": True,
        "defects": [],
        "quarantined_values": [],
        "events": [],
    }

    for field in REQUIRED_FIELDS:
        if field not in summary or summary[field] in (None, ""):
            result["defects"].append(
                {
                    "field": field,
                    "class": "BLOCKER",
                    "reason": "MISSING_REQUIRED_FIELD",
                }
            )

    if "glucose_measurement_date" in summary:
        if not is_valid_iso_date(summary["glucose_measurement_date"]):
            result["defects"].append(
                {
                    "field": "glucose_measurement_date",
                    "class": "BLOCKER",
                    "reason": "INVALID_DATE_FORMAT",
                }
            )

    if "glucose_unit" in summary:
        if summary["glucose_unit"] not in VALID_UNITS:
            result["defects"].append(
                {
                    "field": "glucose_unit",
                    "class": "BLOCKER",
                    "reason": "INVALID_UNIT",
                }
            )

    if "glucose_condition" in summary:
        if summary["glucose_condition"] not in VALID_CONDITIONS:
            result["defects"].append(
                {
                    "field": "glucose_condition",
                    "class": "BLOCKER",
                    "reason": "INVALID_CONDITION",
                }
            )

    if "weight_measurement_date" in summary:
        if not is_valid_iso_date(summary["weight_measurement_date"]):
            result["defects"].append(
                {
                    "field": "weight_measurement_date",
                    "class": "BLOCKER",
                    "reason": "INVALID_DATE_FORMAT",
                }
            )

    blockers = [
        defect
        for defect in result["defects"]
        if defect["class"] == "BLOCKER"
    ]

    warnings = [
        defect
        for defect in result["defects"]
        if defect["class"] == "WARNING"
    ]

    if blockers:
        result["status"] = "BLOCKED"
        result["data_complete"] = False
    elif warnings:
        result["status"] = "READY_WITH_WARNINGS"
        result["data_complete"] = True
    else:
        result["status"] = "READY_FOR_PHYSICIAN"
        result["data_complete"] = True

    result["events"].append("STATUS_COMPUTED")
    result["events"].append("FLAG_COMPUTED")

    return result


def process(summary):
    return validate_summary(summary)

def process(summary):
    return validate_summary(summary)
