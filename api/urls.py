from django.urls import path, include
from rest_framework import routers

from api.serializers import ReceiptSerializer
from .views import AccountViewSets, CardViewSets, CustomerViewSets, LoanViewSets, NotificationsViewSets, ReceiptViewSets, TransactionViewSets, WalletViewSets

router = routers.DefaultRouter()
router.register(r"customers", CustomerViewSets)
router.register(r"wallets", WalletViewSets)
router.register(r"accounts", AccountViewSets)
router.register(r"cards", CardViewSets)
router.register(r"transactions", TransactionViewSets)
router.register(r"loans", LoanViewSets)
router.register(r"receipts", ReceiptViewSets)
router.register(r"notifications", NotificationsViewSets)
urlpatterns= [
    path("", include(router.urls))
]