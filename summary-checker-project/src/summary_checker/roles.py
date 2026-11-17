FORBIDDEN_ACTIONS = {
    "executor": [
        "classify_defect",
        "change_status",
    ],
    "reviewer": [
        "change_status",
        "change_criticality",
    ],
    "external_reviewer": [
        "edit_journal",
        "participate_in_development",
    ],
}


def is_allowed(actor_role, action):
    forbidden = FORBIDDEN_ACTIONS.get(actor_role, [])

    return action not in forbidden


def run_check(actor_role):
    return {
        "allowed": is_allowed(actor_role, "run_check"),
    }


def classify_defect(actor_role):
    return {
        "allowed": is_allowed(actor_role, "classify_defect"),
    }


def change_status(actor_role):
    return {
        "allowed": is_allowed(actor_role, "change_status"),
    }


def change_criticality(actor_role):
    return {
        "allowed": is_allowed(actor_role, "change_criticality"),
    }


def edit_journal(actor_role):
    return {
        "allowed": is_allowed(actor_role, "edit_journal"),
    }


def participate_in_development(actor_role):
    return {
        "allowed": is_allowed(actor_role, "participate_in_development"),
    }
