from datetime import datetime
from decimal import Decimal

from account.models import Account
from rest_framework import status
from rest_framework.test import APITestCase
from transaction.models import Transaction


class TransactionAPIViewTest(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(account_id=12345, balance=500)

    def test_create_transaction_success(self):
        response = self.client.post(
            "/transaction/",
            {
                "account": 12345,
                "operation": "P",
                "amount": 100,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["account"], 1)
        self.assertEqual(response.data["operation"], "P")
        self.assertEqual(Decimal(response.data["amount"]), Decimal(100))
        self.assertEqual(
            datetime.fromisoformat(response.data["event_date"]).date(),
            datetime.now().date(),
        )

    def test_create_transaction_account_not_found(self):
        response = self.client.post(
            "/transaction/",
            {
                "account": 123456,
                "operation": "P",
                "amount": 100,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Não encontrado.")

    def test_create_transaction_negative_balance(self):
        response = self.client.post(
            "/transaction/",
            {
                "account": 12345,
                "operation": "D",
                "amount": 600,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["balance"], "Saldo não pode ser negativo")

    def test_create_transaction_invalid_operation(self):
        response = self.client.post(
            "/transaction/",
            {
                "account": 12345,
                "operation": "X",
                "amount": 100,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["operation"][0], '"X" não é um escolha válido.')
