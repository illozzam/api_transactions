from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("account/", include(("account.urls", "account"), namespace="account")),
    path(
        "transaction/",
        include(("transaction.urls", "transaction"), namespace="transaction"),
    ),
    path("admin/", admin.site.urls),
]
