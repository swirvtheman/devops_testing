# Övning 11 - Bankkonto med TDD

Bygg en BankAccount-klass med TDD.

## Funktionalitet

- Skapa konto (startsaldo 0 SEK)
- Insättning (deposit)
- Uttag (withdraw)
- Kontrollera saldo (balance)
- Transaktionshistorik (history)
- Felhantering
  - Kan inte sätta in negativt belopp
  - Kan inte ta ut mer än saldot
  - Kan inte ta ut negativt belopp

## Krav och mål

- Minst tio (10) tester innan klassen är klar.
- Följ RED-GREEN-REFACTOR strikt.

## Förslag på testordning

1. test_new_account_has_zero_balance
 2. test_deposit_increases_balance
 3. test_deposit_specific_amount
 4. test_withdraw_decreases_balance
 5. test_withdraw_specific_amount
 6. test_deposit_negative_raises_error
 7. test_withdraw_more_than_balance_raises_error
 8. test_withdraw_negative_raises_error
 9. test_transaction_history_records_deposits
10. test_transaction_history_records_withdrawals
11. test_multiple_transactions_in_history
12. test_balance_after_multiple_operations

## BONUSUTMANINGAR

- Överföringar mellan konton (transfer)
- Ränteberäkning
- Kontoutdrag som formatterad sträng

