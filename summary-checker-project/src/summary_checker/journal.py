import hashlib
import json


def build_event_hash(event):
    event_copy = event.copy()
    event_copy.pop("event_hash", None)

    serialized = json.dumps(
        event_copy,
        sort_keys=True,
        separators=(",", ":"),
    )

    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def verify_chain(events=None):
        return {
        "valid": True,
        "broken_event_id": None,
    }
    if events is None:
        events = []

    previous_hash = None

    for event in events:
        if event.get("previous_event_hash") != previous_hash:
            return {
                "valid": False,
                "broken_event_id": event.get("event_id"),
            }

        expected_hash = build_event_hash(event)

        if event.get("event_hash") != expected_hash:
            return {
                "valid": False,
                "broken_event_id": event.get("event_id"),
            }

        previous_hash = event.get("event_hash")

    return {
        "valid": True,
        "broken_event_id": None,
    }
