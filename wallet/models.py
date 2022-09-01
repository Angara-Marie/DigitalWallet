
from django.db import models
from django.utils import timezone


class Customer(models.Model):
   first_name = models.CharField(max_length= 20,null=True)
   last_name = models.CharField(max_length= 20,null=True)
   address = models.TextField(default='')
   email = models.EmailField()
   phone_number = models.CharField(max_length= 15,null=True)
   gender = models.CharField(max_length= 10,null=True)
   age = models.PositiveSmallIntegerField()
   password = models.CharField(max_length=10,null=True)
   id_number = models.IntegerField()
   nationality = models.CharField(max_length=15,null=True)
   date_of_registeration = models.DateTimeField(default=timezone.now)
   profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')


class Wallet(models.Model):
   balance = models.IntegerField()
   customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='Wallet_customer')
   date_created = models.DateTimeField(default=timezone.now)
   status = models.CharField(max_length=10,null=True)
   pin = models.IntegerField()
   currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='Wallet_currency')


class Account(models.Model):
   account_number = models.IntegerField()
   account_type = models.CharField(max_length=10,null=True)
   balance = models.IntegerField()
   account_name = models.CharField(max_length=15,null=True)
   # customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='Account_customer')
   wallet =models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='Wallet_account')


class Transaction(models.Model):
   transaction_REF = models.CharField(max_length=20,null=True)
   wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='Transaction_wallet')
   transaction_amount = models.IntegerField()
   transaction_number = models.IntegerField()
   transaction_type = models.CharField(max_length=10,null=True)
   transaction_charge = models.IntegerField ()
   origin_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_origin')
   destination_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination')
   date = models.DateTimeField(default=timezone.now)
   time = models.DateTimeField(default=timezone.now)


class Card(models.Model):
   card_number = models.IntegerField()
   card_name = models.CharField(max_length=15,null=True)
   date_issued = models.DateTimeField(default=timezone.now)
   card_type = models.CharField(max_length=10,null=True)
   expiry_date = models.DateTimeField(default=timezone.now)
   cvv = models.IntegerField()
   wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='Card_wallet')
   account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name= 'Card_account')
   issuer = models.CharField(max_length=10,null=True)


class Third_party(models.Model):
   name = models.CharField(max_length=20,null=True)
   transaction_cost = models.IntegerField()
   account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name= 'Third_party_account')
   currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name= 'Third_party_currency')


class Notifications(models.Model):
   message = models.TextField(default= '')
   title = models.CharField(max_length=20,null=True)
   recepient = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='Notifications_recepient')
   status = models.CharField(max_length=10,null=True)
   date = models.DateTimeField(default=timezone.now)



class Receipt(models.Model):
   receipt_type = models.CharField(max_length=10,null=True)
   receipt_date = models.DateTimeField(default=timezone.now)
   receipt_file = models.FileField()
   total_amount = models.IntegerField()
   transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='Receipt_transaction')

class Loan(models.Model):
   loan_id = models.IntegerField()
   loan_type = models.CharField(max_length=20,null=True)
   amount = models.IntegerField()
   name = models.CharField(max_length=15,null=True)
   loan_status = models.CharField(max_length=10,null=True)
   date = models.DateTimeField(default=timezone.now)
   wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='Loan_wallet')
   interest_rate = models.IntegerField()
   payment_due_date = models.DateTimeField(default=timezone.now)
   loan_balance = models.IntegerField()
   guarantor = models. ForeignKey('Customer', on_delete=models.CASCADE, related_name='Loan_guarantor')


class Reward(models.Model):
   recipient = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='Reward_wallet')
   date_of_reward = models.DateTimeField(default=timezone.now)
   points = models.IntegerField()
   transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='Reward_transaction')  

class Currency(models.Model):
   country_of_origin = models.CharField(max_length=10,null=True)
   amount = models.IntegerField()
   symbol = models.CharField(max_length=5,null=True)

# class  AccountEntry(models.Model):
#    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='account_entries')
#    entry_date = models.DateTimeField(default=timezone.now) 
#    debit_amount = models.DecimalField(max_digits=9 , decimal_places=2)
#    credit_amount = models.DecimalField(max_digits=9 , decimal_places=2)
#    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name= 'accountentry_currency')
#    description = models.CharField(max_length=255, null=True, blank=True)

