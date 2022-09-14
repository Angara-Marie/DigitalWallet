# importing the library called forms
from dataclasses import field, fields
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, Third_party, Transaction, Wallet
from django.forms import ModelForm
#creating a class to represent the form we want to create

class CustomerRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Customer
        fields="__all__"

class CustomerWalletForm(ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"        

class CustomerAccountForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"      

class CustomerTransactionForm(ModelForm):
    class Meta:
        model=Transaction
        fields="__all__" 

class CustomerCardForm(ModelForm):
    class Meta:
        model=Card
        fields="__all__" 

class CustomerThird_partyForm(ModelForm):
    class Meta:
        model=Third_party
        fields="__all__" 

class CustomerNotificationsForm(ModelForm):
    class Meta:
        model=Notifications
        fields="__all__" 

class CustomerReceiptForm(ModelForm):
    class Meta:
        model=Receipt
        fields="__all__" 

class CustomerLoanForm(ModelForm):
    class Meta:
        model=Loan
        fields="__all__" 

class CustomerRewardForm(ModelForm):
    class Meta:
        model=Reward
        fields="__all__" 

class CustomerCurrencyForm(ModelForm):
    class Meta:
        model=Currency
        fields="__all__" 

                                                                           