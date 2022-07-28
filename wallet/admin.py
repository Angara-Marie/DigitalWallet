from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import Third_party
from .models import Notifications
from .models import Receipt
from .models import Loan
from .models import Reward
from .models import Currency

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('first_name', 'last_name')
admin.site.register(Customer, CustomerAdmin) 
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notifications)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Currency)


# class WalletAdmin(admin.ModelAdmin):
#     list_display = ('balance', 'date_created', 'status', 'pin', Customer,Currency )
#     search_fields = ('status', 'date_created')
# admin.site.register(Wallet, WalletAdmin) 

# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('account_name','account_number', 'account_type', 'balance', Wallet)
#     search_fields = ('account_name', 'account_type')
# admin.site.register(Account, AccountAdmin)   


# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('transaction_REF', Wallet,'transaction_amount', 'transaction_number', 'transaction_type', Receipt, 'transaction_charge', Account, 'date', 'time')
#     search_fields = ('transaction_REF', Account)
# admin.site.register(Transaction, TransactionAdmin) 


# class CardAdmin(admin.ModelAdmin):
#     list_display = ('card_name', 'card_number','date_issued', 'card_type', 'expiry_date', 'cvv', Wallet, Account, 'issuer')
#     search_fields = ('card_number', 'issuer')
# admin.site.register(Card, CardAdmin)


# class Third_partyAdmin(admin.ModelAdmin):
#     list_display = ()
#     search_fields = ()
# admin.site.register(Third_party, Third_partyAdmin)



# class NotificationsAdmin(admin.ModelAdmin):
#     list_display = ()
#     search_fields = ()
# admin.site.register(Notifications, NotificationsAdmin)


# class ReceiptAdmin(admin.ModelAdmin):
#     list_display = ()
#     search_fields = ()
# admin.site.register(Receipt, ReceiptAdmin)


# class LoanAdmin(admin.ModelAdmin):
#     list_display = ()
#     search_fields = ()
# admin.site.register(Loan, LoanAdmin)


# class RewardAdmin(admin.ModelAdmin):
#     list_display = ()
#     search_fields = ()
# admin.site.register(Reward, RewardAdmin)


# class CurrencyAdmin(admin.ModelAdmin):
#     list_display = ()
#     search_fields = ()
# admin.site.register(Currency, CurrencyAdmin)


