from django.urls import path, include
from rest_framework import routers
from .views import AccountViewSets, CardViewSets, CustomerViewSets, TransactionViewSets, WalletViewSets

router = routers.DefaultRouter()
router.register(r"customers", CustomerViewSets)
router.register(r"wallets", WalletViewSets)
router.register(r"accounts", AccountViewSets)
router.register(r"cards", CardViewSets)
router.register(r"transactions", TransactionViewSets)
urlpatterns= [
    path("", include(router.urls))
]