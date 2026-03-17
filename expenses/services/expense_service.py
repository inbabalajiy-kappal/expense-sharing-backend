from expenses.models import User, Expense, ExpenseParticipant, Balance
from expenses.services.factory.split_factory import SplitStrategyFactory


class ExpenseService:

    def add_expense(self, payer_id, amount, participants, split_type):

        payer = User.objects.get(id=payer_id)
        users = list(User.objects.filter(id__in=participants))

        strategy = SplitStrategyFactory.get_strategy(split_type)

        shares = strategy.calculate(amount, users)

        expense = Expense.objects.create(
            payer=payer,
            amount=amount,
            split_type=split_type,
        )

        [
            self._persist(expense, payer, user, share)
            for user, share in shares.items()
        ]

        return expense
    def get_all_expenses(self):

        return [
            {
                "id": expense.id,
                "payer_id": expense.payer.id,
                "amount": expense.amount,
                "split_type": expense.split_type,
                "participants": [
                    participant.user.id
                    for participant in expense.expenseparticipant_set.all()
                ],
                "created_at": expense.created_at,
            }
            for expense in Expense.objects.all()
        ]