from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Notifications, Receipt, Transaction, Wallet,Loan
from .serializers import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationsSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer

# Create your views here.

class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializer

class WalletViewSets(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class AccountViewSets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 

class CardViewSets(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class TransactionViewSets(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer  

class LoanViewSets(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class ReceiptViewSets(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class NotificationsViewSets(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer        

