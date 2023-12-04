from account.models import Account
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from transaction.serializers import TransactionSerializer


class TransactionAPIView(ViewSet):
    serializer_class = TransactionSerializer

    def create(self, request):
        try:
            account = get_object_or_404(Account, account_id=request.data["account"])
        except ObjectDoesNotExist:
            return Response({"account": "Conta não existe"}, status=404)

        request.data["account"] = account.id

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=404)

        try:
            serializer.save()
        except ValueError:
            return Response({"balance": "Saldo não pode ser negativo"}, status=404)

        return Response(serializer.data, status=201)
