from django.urls import path
from transaction.views import TransactionAPIView

urlpatterns = [
    path(
        "",
        TransactionAPIView.as_view({"post": "create"}),
        name="transaction",
    ),
]
