from decimal import Decimal

from django.db import models


class Transaction(models.Model):
    operation_choices = (("D", "Débito"), ("C", "Crédito"), ("P", "PIX"))

    account = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, related_name="transactions"
    )
    operation = models.CharField(max_length=1, choices=operation_choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.operation} - {self.amount}"

    def save(self, *args, **kwargs):
        if self.operation == "D":
            self.amount += self.amount * Decimal(0.03)
        elif self.operation == "C":
            self.amount += self.amount * Decimal(0.05)

        self.account.balance -= self.amount
        self.account.save()
        super().save(*args, **kwargs)
