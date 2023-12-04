from decimal import Decimal

from account.models import Account
from rest_framework import status
from rest_framework.test import APITestCase


class AccountAPIViewTest(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(account_id=12345, balance=1000)

    def test_get_account_success(self):
        response = self.client.get("/account/?account_id=12345")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["account_id"], self.account.account_id)
        self.assertEqual(Decimal(response.data["balance"]), self.account.balance)

    def test_get_account_not_found(self):
        response = self.client.get("/account/?account_id=999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_account_success(self):
        response = self.client.post(
            "/account/", {"account_id": 1349, "balance": 790}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["account_id"], 1349)
        self.assertEqual(Decimal(response.data["balance"]), Decimal(790))

    def test_create_account_negative_balance(self):
        response = self.client.post(
            "/account/", {"account_id": 1349, "balance": -790}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["balance"][0],
            "Certifique-se que este valor é maior ou igual a 0.",
        )
