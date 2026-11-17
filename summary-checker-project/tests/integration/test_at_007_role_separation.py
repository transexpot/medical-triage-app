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

from summary_checker.roles import (
    classify_defect,
    change_criticality,
    change_status,
    edit_journal,
    participate_in_development,
    run_check,
)


class TestAT007RoleSeparation(unittest.TestCase):
    def test_roles_cannot_perform_forbidden_actions(self):
        executor_check = run_check("executor")

        self.assertFalse(executor_check["allowed"])

        executor_classification = classify_defect("executor")

        self.assertFalse(executor_classification["allowed"])

        executor_status = change_status("executor")

        self.assertFalse(executor_status["allowed"])

        reviewer_status = change_status("reviewer")

        self.assertFalse(reviewer_status["allowed"])

        reviewer_criticality = change_criticality("reviewer")

        self.assertFalse(reviewer_criticality["allowed"])

        external_journal = edit_journal("external_reviewer")

        self.assertFalse(external_journal["allowed"])

        external_development = participate_in_development(
            "external_reviewer"
        )

        self.assertFalse(external_development["allowed"])


if __name__ == "__main__":
    unittest.main()
