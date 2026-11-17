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


def is_valid_iso_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (TypeError, ValueError):
        return False


def has_blocker(summary):
    for field in REQUIRED_FIELDS:
        if field not in summary or summary[field] in (None, ""):
            return True

    if not is_valid_iso_date(summary["glucose_measurement_date"]):
        return True

    return False


def reschedule(summary, appointment_date):
    result = {
        "status": "RESCHEDULED",
        "data_complete": True,
        "events": [],
    }

    if not is_valid_iso_date(appointment_date):
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["events"].append("INVALID_APPOINTMENT_DATE")
        return result

    if has_blocker(summary):
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["events"].append("BLOCKER_PRESENT")

        if appointment_date < summary["glucose_measurement_date"]:
            result["events"].append("DEADLINE_MISSED")

        return result

    if not is_valid_iso_date(summary["glucose_measurement_date"]):
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["events"].append("INVALID_GLUCOSE_DATE")
        return result

    if appointment_date <= summary["glucose_measurement_date"]:
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["events"].append("APPOINTMENT_NOT_IN_FUTURE")
        return result

    result["events"].append("CHECKS_PRESERVED")
    result["events"].append("APPOINTMENT_RESCHEDULED")

    return result
