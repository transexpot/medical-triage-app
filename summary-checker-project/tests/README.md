# Tests

Таблица ниже — фактическая трассируемость
между acceptance-кейсами и тестовыми файлами.

| Acceptance-кейс | Тестовый файл | Тестовый кейс | Статус покрытия | Примечание |
|---|---|---|---|---|
| AT-001 | test_at_001_valid_summary.py | test_valid_summary_is_ready_for_physician | COVERED | Проверяет валидную сводку |
| AT-002 | test_at_002_missing_glucose_date.py | test_missing_glucose_date_is_blocked | COVERED | Проверяет отсутствие даты глюкозы |
| AT-003 | test_at_003_invalid_weight_date_format.py | test_invalid_weight_date_format_is_warning | COVERED | Проверяет неверный формат даты веса |
| AT-004 | test_at_004_unknown_source.py | test_unknown_source_needs_clarification | COVERED | Проверяет неизвестный источник |
| AT-005A | test_at_005a_reschedule_future.py | test_reschedule_to_future_preserves_checks | COVERED | Проверяет перенос на будущую дату |
| AT-005B_COMPLETE | test_at_005b_complete_past_deadline.py | test_past_deadline_with_complete_data | COVERED | Проверяет перенос на прошлое при полных данных |
| AT-005B_BLOCKER | test_at_005b_blocker_past_deadline.py | test_past_deadline_with_blocker | COVERED | Проверяет перенос на прошлое при блокере |
| AT-005C | test_at_005c_double_reschedule.py | test_double_reschedule_uses_latest_deadline | COVERED | Проверяет двойной перенос |
| AT-005D | test_at_005d_cancel_appointment.py | test_cancel_appointment_archives_summary | COVERED | Проверяет отмену приёма |
| AT-005E | test_at_005e_cancel_and_reschedule.py | test_cancel_then_reschedule_dearchives_summary | COVERED | Проверяет отмену и повторное назначение |
| AT-006 | test_at_006_journal_integrity.py | test_journal_chain_is_valid | COVERED | Проверяет целостность журнала |
| AT-007 | test_at_007_role_separation.py | test_roles_cannot_perform_forbidden_actions | COVERED | Проверяет разделение полномочий |
| AT-008 | test_at_008_metrics_ground_truth.py | test_metrics_match_ground_truth | COVERED | Проверяет метрики против ground truth |
| AT-009 | test_at_009_determinism.py | test_same_input_gives_same_result | COVERED | Проверяет детерминизм |
