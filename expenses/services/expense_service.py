from decimal import Decimal
from django.db.models import Q

from expenses.models import User, Expense, ExpenseParticipant, Balance


class ExpenseService:
    SUPPORTED_SPLIT = "EQUAL"

    def add_expense(self, payer_id, amount, participants, split_type="EQUAL"):
        self._validate_split(split_type)

        payer = User.objects.get(id=payer_id)
        users = self._fetch_participants(participants)

        expense = Expense.objects.create(
            payer=payer,
            amount=amount,
            split_type=split_type,
        )

        share = round(Decimal(amount) / len(users), 2)

        [
            self._create_participant_and_balance(expense, payer, user, share)
            for user in users
        ]

        return expense

    def _validate_split(self, split_type):
        split_type == self.SUPPORTED_SPLIT or self._raise_invalid_split()

    def _raise_invalid_split(self):
        raise ValueError("Only EQUAL split is supported.")

    def _fetch_participants(self, participants):
        users = list(User.objects.filter(id__in=participants))
        len(users) == len(participants) or self._raise_invalid_participant()
        return users

    def _raise_invalid_participant(self):
        raise ValueError("Invalid participant ID detected.")

    def _create_participant_and_balance(self, expense, payer, user, share):
        ExpenseParticipant.objects.create(
            expense=expense,
            user=user,
            share=share,
        )

        (user.id != payer.id) and self._update_balance(
            debtor=user,
            creditor=payer,
            amount=share,
        )

    def _update_balance(self, debtor, creditor, amount):
        reverse = Balance.objects.filter(
            debtor=creditor,
            creditor=debtor,
        ).first()

        reverse_amount = getattr(reverse, "amount", Decimal("0"))

        adjusted_amount = max(amount - reverse_amount, Decimal("0"))
        remaining_reverse = max(reverse_amount - amount, Decimal("0"))

        reverse and self._handle_reverse(reverse, remaining_reverse)

        adjusted_amount and self._increase_balance(
            debtor,
            creditor,
            adjusted_amount,
        )

    def _handle_reverse(self, reverse, remaining_reverse):
        remaining_reverse and self._save_reverse(reverse, remaining_reverse) or reverse.delete()

    def _save_reverse(self, reverse, amount):
        reverse.amount = amount
        reverse.save()

    def _increase_balance(self, debtor, creditor, amount):
        balance, _ = Balance.objects.get_or_create(
            debtor=debtor,
            creditor=creditor,
            defaults={"amount": 0},
        )

        balance.amount += amount
        balance.save()

    def get_all_balances(self):
        return [
            self._format_balance(balance)
            for balance in Balance.objects.filter(amount__gt=0)
        ]

    def get_user_balances(self, user_id):
        balances = Balance.objects.filter(
            amount__gt=0
        ).filter(
            Q(debtor_id=user_id) | Q(creditor_id=user_id)
        )

        return [
            self._format_balance(balance)
            for balance in balances
        ]

    def _format_balance(self, balance):
        return f"{balance.debtor.name} owes {balance.creditor.name} {balance.amount:.0f}"