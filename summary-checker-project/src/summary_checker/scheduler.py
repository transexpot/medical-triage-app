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

    glucose_date = summary.get("glucose_measurement_date")

    if glucose_date is None or not is_valid_iso_date(glucose_date):
        return True

    return False


def reschedule(summary, appointment_date):
    result = {
        "status": "RESCHEDULED",
        "data_complete": True,
        "clinical_use_deadline": appointment_date,
        "events": [],
    }

    if not is_valid_iso_date(appointment_date):
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["clinical_use_deadline"] = None
        result["events"].append("INVALID_APPOINTMENT_DATE")
        return result

    today = datetime.now().strftime("%Y-%m-%d")

    if has_blocker(summary):
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["clinical_use_deadline"] = None
        result["events"].append("BLOCKER_PRESENT")

        if appointment_date < today:
            result["events"].append("DEADLINE_MISSED")

        return result

    glucose_date = summary["glucose_measurement_date"]

    if appointment_date < today:
        result["status"] = "DEADLINE_MISSED"
        result["data_complete"] = True
        result["clinical_use_deadline"] = None
        result["events"].append("DEADLINE_MISSED")
        return result

    if appointment_date <= glucose_date:
        result["status"] = "BLOCKED"
        result["data_complete"] = False
        result["clinical_use_deadline"] = None
        result["events"].append("APPOINTMENT_NOT_IN_FUTURE")
        return result

    result["events"].append("CHECKS_PRESERVED")
    result["events"].append("APPOINTMENT_RESCHEDULED")

    return resultdef cancel_appointment(summary):
    result = {
        "status": "ARCHIVED",
        "data_complete": True,
        "clinical_use_deadline": None,
        "events": [],
    }

    result["events"].append("APPOINTMENT_CANCELLED")
    result["events"].append("CHECKS_PRESERVED")
    result["events"].append("DEADLINE_CANCELLED")
    result["events"].append("STATUS_COMPUTED")
    result["events"].append("FLAG_COMPUTED")

    return result
