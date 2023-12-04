from rest_framework import serializers
from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "account",
            "operation",
            "amount",
            "event_date",
        )
        read_only_fields = ("event_date",)
