from account.views import AccountAPIView
from django.urls import path

urlpatterns = [
    path(
        "",
        AccountAPIView.as_view({"get": "retrieve", "post": "create"}),
        name="account_view",
    ),
]
