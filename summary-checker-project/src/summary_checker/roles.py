ROLE_PERMISSIONS = {
    "executor": [
        "run_check",
        "classify_defect",
        "change_status",
    ],
    "physician": [
        "review_summary",
        "approve_summary",
        "request_changes",
    ],
    "auditor": [
        "view_journal",
        "view_metrics",
    ],
}


def has_permission(role, action):
    if role not in ROLE_PERMISSIONS:
        return False

    return action in ROLE_PERMISSIONS[role]


def classify_defect(role, defect):
    if not has_permission(role, "classify_defect"):
        return {
            "allowed": False,
            "reason": "Role is not allowed to classify defects",
        }

    return {
        "allowed": True,
        "defect": defect,
    }


def change_criticality(role, criticality):
    if not has_permission(role, "change_status"):
        return {
            "allowed": False,
            "reason": "Role is not allowed to change criticality",
        }

    return {
        "allowed": True,
        "criticality": criticality,
    }


def change_status(role, status):
    if not has_permission(role, "change_status"):
        return {
            "allowed": False,
            "reason": "Role is not allowed to change status",
        }

    return {
        "allowed": True,
        "status": status,
    }


def edit_journal(role, entry):
    if not has_permission(role, "edit_journal"):
        return {
            "allowed": False,
            "reason": "Role is not allowed to edit journal",
        }

    return {
        "allowed": True,
        "entry": entry,
    }



def edit_journal(role, entry):
    if not has_permission(role, "edit_journal"):
        return {
            "allowed": False,
            "reason": "Role is not allowed to edit journal",
        }

    return {
        "allowed": True,
        "entry": entry,
    }
