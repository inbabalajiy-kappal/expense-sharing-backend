from decimal import Decimal

from expenses.models import Expense
from expenses.repositories.balance_repo import BalanceRepository
from expenses.repositories.participant_repo import ExpenseParticipantRepository
from expenses.repositories.user_repo import UserRepository
from expenses.services.factory.split_factory import SplitFactory


class ExpenseService:

    def __init__(
        self,
        expense_model=None,
        user_repo=None,
        participant_repo=None,
        balance_repo=None,
    ):
        self.expense_model = expense_model or Expense
        self.user_repo = user_repo or UserRepository()
        self.participant_repo = participant_repo or ExpenseParticipantRepository()
        self.balance_repo = balance_repo or BalanceRepository()

    def add_expense(self, payer_id, amount, participants, split_type, metadata=None):

        payer = self.user_repo.get_by_id(payer_id)
        users = self.user_repo.get_many_by_ids(participants)
        shares = self._compute_shares(amount, users, split_type, metadata)
        expense = self._create_expense(payer, amount, split_type)
        self._record_participants(expense, payer, shares)

        return expense

    def get_all_expenses(self):

        return [
            self._to_expense_dict(expense)
            for expense in self.expense_model.objects.all()
        ]

    def get_all_balances(self):

        return [
            self._to_balance_dict(balance)
            for balance in self.balance_repo.get_all()
            if balance.amount > 0
        ]

    def _compute_shares(self, amount, users, split_type, metadata):

        return SplitFactory.create(split_type).calculate(amount, users, metadata)

    def _create_expense(self, payer, amount, split_type):

        return self.expense_model.objects.create(
            payer=payer,
            amount=amount,
            split_type=split_type,
        )

    def _record_participants(self, expense, payer, shares):

        for user, share in shares.items():
            self._record_participant(expense, payer, user, share)

    def _record_participant(self, expense, payer, user, share):

        self.participant_repo.create(expense, user, share)

        if user.id != payer.id:
            self.balance_repo.update_balance(user, payer, Decimal(share))

    def _to_expense_dict(self, expense):

        return {
            "id": expense.id,
            "payer_id": expense.payer.id,
            "amount": expense.amount,
            "split_type": expense.split_type,
            "participants": [p.user.id for p in expense.participants.all()],
            "created_at": expense.created_at,
        }

    def _to_balance_dict(self, balance):

        return {
            "debtor_id": balance.debtor.id,
            "creditor_id": balance.creditor.id,
            "amount": balance.amount,
        }
