import os
import sys
import unittest


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "src",
        )
    ),
)

from summary_checker.journal import build_event_hash, verify_chain


class TestAT006JournalIntegrity(unittest.TestCase):
    def test_journal_chain_is_valid(self):
        first_event = {
            "event_id": "EVT-001",
            "summary_id": "SUM-001",
            "event_type": "SUMMARY_CREATED",
            "sequence": 1,
            "occurred_at": "2026-11-17T10:00:00Z",
            "actor_id": "USER-001",
            "actor_role": "executor",
            "schema_version": "1.0",
            "payload": {
                "summary_id": "SUM-001",
            },
            "previous_event_hash": None,
        }

        first_event["event_hash"] = build_event_hash(first_event)

        second_event = {
            "event_id": "EVT-002",
            "summary_id": "SUM-001",
            "event_type": "STATUS_COMPUTED",
            "sequence": 2,
            "occurred_at": "2026-11-17T10:01:00Z",
            "actor_id": "SYSTEM",
            "actor_role": "system",
            "schema_version": "1.0",
            "payload": {
                "status": "READY_FOR_PHYSICIAN",
            },
            "previous_event_hash": first_event["event_hash"],
        }

        second_event["event_hash"] = build_event_hash(second_event)

        events = [
            first_event,
            second_event,
        ]

        result = verify_chain(events)

        self.assertTrue(result["valid"])

        self.assertIsNone(result["broken_event_id"])

    def test_broken_hash_is_detected(self):
        first_event = {
            "event_id": "EVT-001",
            "summary_id": "SUM-001",
            "event_type": "SUMMARY_CREATED",
            "sequence": 1,
            "occurred_at": "2026-11-17T10:00:00Z",
            "actor_id": "USER-001",
            "actor_role": "executor",
            "schema_version": "1.0",
            "payload": {
                "summary_id": "SUM-001",
            },
            "previous_event_hash": None,
        }

        first_event["event_hash"] = build_event_hash(first_event)

        second_event = {
            "event_id": "EVT-002",
            "summary_id": "SUM-001",
            "event_type": "STATUS_COMPUTED",
            "sequence": 2,
            "occurred_at": "2026-11-17T10:01:00Z",
            "actor_id": "SYSTEM",
            "actor_role": "system",
            "schema_version": "1.0",
            "payload": {
                "status": "READY_FOR_PHYSICIAN",
            },
            "previous_event_hash": first_event["event_hash"],
        }

        second_event["event_hash"] = "broken-hash"

        events = [
            first_event,
            second_event,
        ]

        result = verify_chain(events)

        self.assertFalse(result["valid"])

        self.assertEqual(
            result["broken_event_id"],
            "EVT-002",
        )
