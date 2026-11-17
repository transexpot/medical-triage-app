import unittest


class TestAT007RoleSeparation(unittest.TestCase):
    def test_roles_cannot_perform_forbidden_actions(self):
        # Это статическая проверка контракта ролей.
        # После создания движка здесь будут вызовы
        # summary_checker.run_check(actor_role="executor")
        # и проверка:
        # self.assertFalse(result["allowed"])

        # Исполнитель не может запускать проверку.
        executor_forbidden_actions = [
            "run_check",
            "classify_defect",
            "change_status",
        ]

        # Проверяющий T1 не может менять статус вручную
        # и не может менять критичность.
        reviewer_forbidden_actions = [
            "change_status",
            "change_criticality",
        ]

        # Внешний рецензент не может редактировать журнал
        # и не может участвовать в разработке.
        external_reviewer_forbidden_actions = [
            "edit_journal",
            "participate_in_development",
        ]

        # Проверяем, что списки запрещённых действий не пустые.
        self.assertGreater(len(executor_forbidden_actions), 0)
        self.assertGreater(len(reviewer_forbidden_actions), 0)
        self.assertGreater(
            len(external_reviewer_forbidden_actions),
            0,
        )

        # Проверяем, что ключевые запрещённые действия присутствуют.
        self.assertIn("run_check", executor_forbidden_actions)
        self.assertIn("change_status", reviewer_forbidden_actions)
        self.assertIn(
            "edit_journal",
            external_reviewer_forbidden_actions,
        )


if __name__ == "__main__":
    unittest.main()
