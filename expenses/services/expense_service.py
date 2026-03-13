
from django.db.models import Q
from expenses.models import User, Expense, ExpenseParticipant, Balance


class ExpenseService:

    def add_expense(self, payer_id, amount, participants, split_type="EQUAL"):
        """
        Add an expense and update balances.
        """

        if split_type != "EQUAL":
            raise ValueError("Only EQUAL split is supported.")

        payer = User.objects.get(id=payer_id)
        participant_users = list(User.objects.filter(id__in=participants))

        if len(participant_users) != len(participants):
            raise ValueError("Invalid participant ID detected.")

        expense = Expense.objects.create(
            payer=payer,
            amount=amount,
            split_type=split_type,
        )

        share = round(amount / len(participants), 2)

        for user in participant_users:
            ExpenseParticipant.objects.create(
                expense=expense,
                user=user,
                share=share,
            )

            if user.id != payer_id:
                self._update_balance(
                    debtor=user,
                    creditor=payer,
                    amount=share,
                )

        return expense

    def _update_balance(self, debtor, creditor, amount):
        """
        Handles reverse balances properly.
        """

        reverse = Balance.objects.filter(
            debtor=creditor,
            creditor=debtor
        ).first()

        if reverse:
            if reverse.amount > amount:
                reverse.amount -= amount
                reverse.save()
                return
            elif reverse.amount == amount:
                reverse.delete()
                return
            else:
                amount -= reverse.amount
                reverse.delete()

        balance, created = Balance.objects.get_or_create(
            debtor=debtor,
            creditor=creditor,
            defaults={"amount": 0},
        )

        balance.amount += amount
        balance.save()

    def get_all_balances(self):
        balances = Balance.objects.filter(amount__gt=0)
        return [
            f"{b.debtor.name} owes {b.creditor.name} {b.amount:.0f}"
            for b in balances
        ]

    def get_user_balances(self, user_id):
        balances = Balance.objects.filter(amount__gt=0).filter(
            Q(debtor_id=user_id) | Q(creditor_id=user_id)
        )

        return [
            f"{b.debtor.name} owes {b.creditor.name} {b.amount:.0f}"
            for b in balances
        ]