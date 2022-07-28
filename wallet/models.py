from locale import currency
import re
from django.db import models

class Customer(models.Model):
   first_name = models.CharField(max_length= 20)
   last_name = models.CharField(max_length= 20)
   address = models.TextField()
   email = models.EmailField()
   phone_number = models.CharField(max_length= 15)
   gender = models.CharField(max_length= 10)
   age = models.PositiveSmallIntegerField()


class Wallet(models.Model):
   balance = models.IntegerField()
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wallet_customer')
   date_created = models.DateTimeField()
   status = models.CharField(max_length=10)
   pin = models.IntegerField()
   currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='wallet_currency')


class Account(models.Model):
   account_number = models.IntegerField()
   account_type = models.CharField(max_length=10)
   balance = models.IntegerField()
   account_name = models.CharField(max_length=15)
   wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='account_wallet')


class Transaction(models.Model):
   transaction_REF = models.CharField(max_length=20)
   wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transaction_wallet')
   transaction_amount = models.IntegerField()
   transaction_number = models.IntegerField()
   transaction_type = models.CharField(max_length=10)
   receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE, related_name='transaction_receipt')
   transaction_charge = models.IntegerField ()
   origin_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction_origin')
   destination_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction_destination')
   date = models.DateTimeField()
   time = models.DateTimeField()


class Card(models.Model):
   card_number = models.IntegerField()
   card_name = models.CharField(max_length=15)
   date_issued = models.DateTimeField()
   card_type = models.CharField(max_length=10)
   expiry_date = models.DateTimeField()
   cvv = models.IntegerField()
   wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='card_wallet')
   account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name= 'card_account')
   issuer = models.CharField(max_length=10)


class Third_party(models.Model):
   name = models.CharField(max_length=20)
   transaction_cost = models.IntegerField()
   account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name= 'third_party_account')
   currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name= 'third_party_currency')


class Notifications(models.Model):
   message = models.CharField(max_length=150)
   title = models.CharField(max_length=20)
   recepient = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notifications_recepient')
   status = models.CharField(max_length=10)
   date = models.DateTimeField()
   time = models.DateTimeField()


class Receipt(models.Model):
   receipt_type = models.CharField(max_length=10)
   receipt_date = models.DateTimeField()
   receipt_file = models.FileField()
   total_amount = models.IntegerField()
   transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='receipt_transaction')

class Loan(models.Model):
   loan_id = models.IntegerField()
   loan_type = models.CharField(max_length=20)
   amount = models.IntegerField()
   name = models.CharField(max_length=15)
   loan_status = models.CharField(max_length=10)
   date = models.DateTimeField()
   time =models.DateTimeField()
   wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='loan_wallet')
   interest_rate = models.IntegerField()
   payment_due_date = models.DateTimeField()
   loan_balance = models.IntegerField()
   guarantor = models. ForeignKey(Customer, on_delete=models.CASCADE, related_name='loan_customer')


class Reward(models.Model):
   recipient = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='reward_wallet')
   date_of_reward = models.DateTimeField()
   points = models.IntegerField()
   transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='reward_transaction')  

class Currency(models.Model):
   country_of_origin = models.CharField(max_length=10)
   amount = models.IntegerField()
   symbol = models.CharField(max_length=2)
