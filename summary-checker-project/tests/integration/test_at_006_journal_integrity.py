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

from summary_checker.journal import verify_chain


class TestAT006JournalIntegrity(unittest.TestCase):
    def test_journal_chain_is_valid(self):
        result = verify_chain()

        self.assertTrue(result["valid"])

        self.assertIsNone(result["broken_event_id"])


if __name__ == "__main__":
    unittest.main()
