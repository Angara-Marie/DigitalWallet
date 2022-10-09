from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "email", "address")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("customer", "balance", "status", "date_created")  

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_name", "account_number", "account_type", "wallet",
         "balance")  

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_name", "card_number", "card_type", "account", "wallet", 
        "issuer", "date_issued","expiry_date", "cvv") 

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction 
        fields = ("transaction_REF", "wallet", "transaction_number", "origin_account",
          "destination_account", "transaction_amount", "transaction_charge", "date")  

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("name","wallet", "loan_id", "loan_status", "loan_type", "amount", "loan_balance",
        "date","payment_due_date", "interest_rate", "guarantor")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("transaction", "receipt_type", "receipt_date", "receipt_file", "total_amount")

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Notifications 
        fields = ("title", "message", "recepient", "status", "date")   