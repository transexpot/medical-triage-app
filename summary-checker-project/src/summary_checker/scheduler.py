from datetime import datetime


def is_valid_iso_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (TypeError, ValueError):
        return False


def reschedule(summary, future_appointment_date):
    result = {
        "status": "RESCHEDULED",
        "events": [],
    }

    if not is_valid_iso_date(future_appointment_date):
        result["status"] = "BLOCKED"
        result["events"].append("INVALID_APPOINTMENT_DATE")
        return result

    if not is_valid_iso_date(summary["glucose_measurement_date"]):
        result["status"] = "BLOCKED"
        result["events"].append("INVALID_GLUCOSE_DATE")
        return result

    if future_appointment_date <= summary["glucose_measurement_date"]:
        result["status"] = "BLOCKED"
        result["events"].append("APPOINTMENT_NOT_IN_FUTURE")
        return result

    result["events"].append("CHECKS_PRESERVED")
    result["events"].append("APPOINTMENT_RESCHEDULED")

    return result
