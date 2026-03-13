from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    SPLIT_CHOICES = (
        ("EQUAL", "Equal"),
    )

    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_type = models.CharField(max_length=10, choices=SPLIT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    participants = models.ManyToManyField(User, related_name="expenses")


class Balance(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="debts")
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credits")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ("debtor", "creditor")

    def __str__(self):
        return f"{self.debtor.name} owes {self.creditor.name} {self.amount}"