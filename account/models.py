from django.db import models


class Account(models.Model):
    account_id = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.account_id)
    
    def save(self, *args, **kwargs):
        """Salva a conta no banco de dados, realizando uma validação para que o saldo não seja negativo em transações financeiras.

        Raises:
            ValueError: Saldo negativo
        """
        if self.balance < 0:
            raise ValueError("Saldo não pode ser negativo")
        super().save(*args, **kwargs)
