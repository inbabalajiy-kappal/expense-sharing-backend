from expenses.models import Balance


class BalanceRepository:

    @staticmethod
    def update_balance(debtor, creditor, amount):

        balance, created = Balance.objects.get_or_create(
            from_user=debtor,
            to_user=creditor,
            defaults={"amount": 0},
        )

        balance.amount += amount
        balance.save()