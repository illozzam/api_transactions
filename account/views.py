from account.models import Account
from account.serializers import AccountSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class AccountAPIView(ViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

    def retrieve(self, request, **kwargs):
        account = get_object_or_404(Account, account_id=request.GET.get("account_id"))
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def create(self, request):
        serializer = AccountSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(e.detail, status=400)

        try:
            serializer.save()
        except ValueError:
            return Response(
                {"balance": ["Certifique-se que este valor é maior ou igual a 0."]},
                status=400,
            )
        return Response(serializer.data, status=201)
