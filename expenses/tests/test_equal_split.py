from expenses.models import Balance
def test_add_expense(self):
    # Arrange: Set up test data
    payer = self.alice
    participants = [self.alice.id, self.bob.id, self.charlie.id]
    amount = 3000

    expense = self.service.add_expense(
        payer_id=payer.id,
        amount=amount,
        participants=participants
    )

    self.assertEqual(expense.amount, 3000)
    self.assertEqual(expense.payer, self.alice)

    balance_bob = Balance.objects.get(debtor=self.bob, creditor=self.alice)
    balance_charlie = Balance.objects.get(debtor=self.charlie, creditor=self.alice)

    self.assertEqual(balance_bob.amount, 1000)
    self.assertEqual(balance_charlie.amount, 1000)