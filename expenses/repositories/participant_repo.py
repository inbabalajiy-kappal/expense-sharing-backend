from decimal import Decimal

from expenses.models import ExpenseParticipant


class ExpenseParticipantRepository:

    def create(self, expense, user, share):

        return ExpenseParticipant.objects.create(
            expense=expense,
            user=user,
            share=Decimal(share),
        )
