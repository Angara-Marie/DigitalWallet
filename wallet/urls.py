from django.urls import path
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
    path("customers/<int:id>/", views.customer_profile, name="customer_profile"),
    path("customers/edit/<int:id>/", views.edit_customer, name="edit_customer"),
    path("wallets/<int:id>/", views.wallet_profile, name="wallet_profile"),
    path("wallets/edit/<int:id>/", views.edit_wallet, name="edit_wallet"),
    path("accounts/<int:id>/", views.account_profile, name="wallet_profile"),
    path("accounts/edit/<int:id>/", views.edit_account, name="edit_account"),
    path("cards/<int:id>/", views.card_profile, name="wallet_profile"),
    path("cards/edit/<int:id>/", views.edit_card, name="edit_account"),
    path("transactions/<int:id>/", views.transaction_profile, name="wallet_profile"),
    path("tranasactions/edit/<int:id>/", views.edit_transaction, name="edit_account"),
    path("receipts/<int:id>/", views.receipt_profile, name="wallet_profile"),
    path("receipts/edit/<int:id>/", views.edit_receipt, name="edit_account"),




    
]