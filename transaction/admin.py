from django.contrib import admin
from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("account", "operation", "amount", "event_date")
    list_filter = ("operation", "event_date")
    search_fields = ("account", "event_date")
