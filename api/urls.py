from django.urls import path, include
from rest_framework import routers
from . import views

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
    path("", include(router.urls)),
    path("deposit/", views.AccountDepositView.as_view(), name="deposit-view"),
    path("withdraw/", views.AccountWithdrawView.as_view(), name="withdraw-view"),
    path("transfer/", views.AccountTransferView.as_view(), name="transfer-view"),
    path("request_loan/", views.AccountRequestLoanView.as_view(), name="request-loan-view"),
    path("repay_loan/", views.AccountRepayLoanView.as_view(), name="repay-loan-view"),
    path("buy_airtime/", views.AccountBuyAirtimeView.as_view(), name="buy-airtime-view"),
]