from decimal import Decimal

from expenses.models import Balance


class BalanceRepository:

    def update_balance(self, debtor, creditor, amount):

        balance, _ = Balance.objects.get_or_create(
            debtor=debtor,
            creditor=creditor,
            defaults={"amount": Decimal("0.00")},
        )

        balance.amount += Decimal(amount)
        balance.save()

    def get_all(self):

        return Balance.objects.all()