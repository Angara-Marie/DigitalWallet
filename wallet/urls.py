from django.urls import path
from .views import customer_account, customer_card, customer_currency, customer_loan, customer_notifications, customer_receipts, customer_reward, customer_thirdparty, customer_transaction, register_customer
from  .views import customer_wallet

urlpatterns = [
    path("register/", register_customer, name="registration"),
    path("wallet/", customer_wallet, name="registration"),
    path("account/",customer_account, name="registration"),
    path("transaction/",customer_transaction, name="registration"),
    path("card/",customer_card, name="registration"),
    path("thirdparty/",customer_thirdparty, name="registration"),
    path("notifications/",customer_notifications, name="registration"),
    path("receipt/",customer_receipts, name="registration"),
    path("loan/",customer_loan, name="registration"),
    path("reward/",customer_reward, name="registration"),
    path("currency/",customer_currency, name="registration"),


    
]