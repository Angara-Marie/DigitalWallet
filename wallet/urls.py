from django.urls import path
# from .views import customer_account, customer_card, customer_currency, customer_loan, customer_notifications, customer_receipts, customer_reward, customer_thirdparty, customer_transaction, register_customer
# from  .views import customer_wallet
from  . import views

urlpatterns = [
    path("register/",views.register_customer, name="registration"),
    path("wallet/",views.customer_wallet, name="wallets"),
    path("account/",views.customer_account, name="accounts"),
    path("transaction/",views.customer_transaction, name="transactions"),
    path("card/",views.customer_card, name="cards"),
    path("thirdparty/",views.customer_thirdparty, name="third_parties"),
    path("notifications/",views.customer_notifications, name="notifications"),
    path("receipt/",views.customer_receipts, name="receipts"),
    path("loan/",views.customer_loan, name="loans"),
    path("reward/",views.customer_reward, name="rewards"),
    path("currency/",views.customer_currency, name="currencies"),
    path("customers/",views.list_customers, name="customers_list"),
    path("wallets/",views.list_wallets, name="wallets_list"),
    path("accounts/",views.list_accounts, name="accounts_list"),
    path("transactions/",views.list_transactions, name="transactions_list"),
    path("cards/",views.list_cards, name="cards_list"),
    path("third_parties/",views.list_third_parties, name="third_parties_list"),
    path("notifications/",views.list_notifications, name="notifications_list"),
    path("receipts/",views.list_receipts, name="receipts_list"),
    path("loans/",views.list_loans, name="loans_list"),
    path("rewards/",views.list_rewards, name="rewards_list"),
    path("currencies/",views.list_currencies, name="currencies_list"),


    
]