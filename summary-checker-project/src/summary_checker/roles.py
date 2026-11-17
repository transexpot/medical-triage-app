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
