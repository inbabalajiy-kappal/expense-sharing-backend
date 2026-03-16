from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Expense(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_type = models.CharField(max_length=20, default='EQUAL')
    created_at = models.DateTimeField(auto_now_add=True)


class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Balance(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debtor')
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creditor')
    amount = models.DecimalField(max_digits=10, decimal_places=2)