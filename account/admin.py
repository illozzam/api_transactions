from account.models import Account
from django.contrib import admin


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_id", "balance")
    search_fields = ("account_id",)
    ordering = ("account_id",)
    list_per_page = 10
