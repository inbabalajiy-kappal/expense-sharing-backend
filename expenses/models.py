# expenses/models.py

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    SPLIT_CHOICES = [
        ("EQUAL", "Equal"),
    ]

    payer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="paid_expenses"
    )

    amount = models.FloatField()
    split_type = models.CharField(
        max_length=20,
        choices=SPLIT_CHOICES,
        default="EQUAL"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payer.name} paid {self.amount}"


class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(
        Expense,
        on_delete=models.CASCADE,
        related_name="participants"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.FloatField()

    def __str__(self):
        return f"{self.user.name} owes {self.share}"


class Balance(models.Model):
    debtor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="debts"
    )
    creditor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="credits"
    )
    amount = models.FloatField(default=0)

    class Meta:
        unique_together = ("debtor", "creditor")

    def __str__(self):
        return f"{self.debtor.name} owes {self.creditor.name} {self.amount}"


class Balance(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="debts")
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credits")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ("debtor", "creditor")

    def __str__(self):
        return f"{self.debtor.name} owes {self.creditor.name} {self.amount}"
