from django.shortcuts import render,redirect
from . import models
from . import forms

def register_customer(request):
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
    {"form":form})

def customer_wallet(request):
    if request.method == "POST":
        form = forms.CustomerWalletForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerWalletForm()        
    return render(request,"wallet/customer_wallet.html",
    {"form":form})

def customer_account(request):
    if request.method == "POST":
        form = forms.CustomerAccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerAccountForm()        
    return render(request,"wallet/customer_account.html",
    {"form":form})

def customer_transaction(request):
    if request.method == "POST":
        form = forms.CustomerTransactionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerTransactionForm()        
    return render(request,"wallet/customer_transaction.html",
    {"form":form})

def customer_card(request):
    if request.method == "POST":
        form = forms.CustomerCardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerCardForm()        
    return render(request,"wallet/customer_card.html",
    {"form":form})    
    
def customer_thirdparty(request):
    if request.method =="POST":
        form = forms.CustomerThird_partyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerThird_partyForm()        
    return render(request,"wallet/customer_thirdparty.html",
    {"form":form})    

def customer_notifications(request):
    if request.method =="POST":
        form = forms.CustomerNotificationsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerNotificationsForm()        
    return render(request,"wallet/customer_notifications.html",
    {"form":form})  

def customer_receipts(request):
    if request.method == "POST":
        form = forms.CustomerReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerReceiptForm()        
    return render(request,"wallet/customer_receipt.html",
    {"form":form})    

def customer_loan(request):
    if request.method == "POST":
        form = forms.CustomerLoanForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerLoanForm()        
    return render(request,"wallet/customer_loan.html",
    {"form":form})     

def customer_reward(request):
    if request.method == "POST":
        form = forms.CustomerRewardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRewardForm()        
    return render(request,"wallet/customer_reward.html",
    {"form":form})     

def customer_currency(request):
    if request.method == "POST":
        form = forms.CustomerCurrencyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerCurrencyForm()        
    return render(request,"wallet/customer_currency.html",
    {"form":form})         


def list_customers(request):
    customers = models.Customer.objects.all()    
    return render(request, "wallet/customers_list.html", 
    {"customers": customers})

def list_wallets(request):
    wallets = models.Wallet.objects.all()  
    return render(request, "wallet/wallets_list.html", 
    {"wallets": wallets})

def list_accounts(request):
    accounts = models.Account.objects.all()
    return render(request, "wallet/accounts_list.html", 
    {"accounts": accounts}) 

def list_transactions(request):
    transactions = models.Transaction.objects.all()
    return render(request, "wallet/transactions_list.html", 
    {"transactions": transactions})    

def list_cards(request):
    cards = models.Card.objects.all()
    return render(request, "wallet/cards_list.html", 
    {"cards": cards})   

def list_third_parties(request):
    third_parties = models.Third_party.objects.all()
    return render(request, "wallet/third_parties_list.html", 
    {"third_parties": third_parties})    

def list_notifications(request):
    notifications = models.Notifications.objects.all()
    return render(request, "wallet/notifications_list.html", 
    {"notifications": notifications})

def list_receipts(request):
    receipts = models.Receipt.objects.all()
    return render(request, "wallet/receipts_list.html", 
    {"receipts": receipts})  

def list_loans(request):
    loans = models.Loan.objects.all()
    return render(request, "wallet/loans_list.html", 
    {"loans": loans})     

def list_rewards(request):
    rewards = models.Reward.objects.all()
    return render(request, "wallet/rewards_list.html", 
    {"rewards": rewards})    

def list_currencies(request):
    currencies = models.Currency.objects.all()
    return render(request, "wallet/currencies_list.html", 
    {"currencies": currencies})  

def customer_profile(request, id):
    customer = models.Customer.objects.get(id=id)  
    return render(request, "wallet/customer_profile.html", 
    {"customer":customer}) 

def edit_customer(request, id):
    customer = models.Customer. objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST,
        instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id)
    else:
        form = forms.CustomerRegistrationForm(instance=customer)
        return render(request, "wallet/edit_customer.html",
        {"form":form}) 

def wallet_profile(request, id):
    wallet = models.Wallet.objects.get(id=id)  
    return render(request, "wallet/wallet_profile.html", 
    {"wallet":wallet})              

def edit_wallet(request, id):
    wallet = models.Wallet. objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerWalletForm(request.POST,
        instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile", id=wallet.id)
    else:
        form = forms.CustomerWalletForm(instance=wallet)
        return render(request, "wallet/edit_wallet.html",
        {"form":form})

def account_profile(request, id):
    account = models.Account.objects.get(id=id)  
    return render(request, "wallet/account_profile.html", 
    {"account":account})          

def edit_account(request, id):
    account = models.Account. objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerAccountForm(request.POST,
        instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile", id=account.id)
    else:
        form = forms.CustomerAccountForm(instance=account)
        return render(request, "wallet/edit_account.html",
        {"form":form}) 

def card_profile(request, id):
    card = models.Card.objects.get(id=id)  
    return render(request, "wallet/card_profile.html", 
    {"card":card})        

def edit_card(request, id):
    card = models.Card. objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerCardForm(request.POST,
        instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_profile", id=card.id)
    else:
        form = forms.CustomerCardForm(instance=card)
        return render(request, "wallet/edit_card.html",
        {"form":form}) 

def transaction_profile(request, id):
    transaction = models.Transaction.objects.get(id=id)  
    return render(request, "wallet/transaction_profile.html", 
    {"transaction":transaction})        

def edit_transaction(request, id):
    transaction = models.Transaction. objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerTransactionForm(request.POST,
        instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile", id=transaction.id)
    else:
        form = forms.CustomerTransactionForm(instance=transaction)
        return render(request, "wallet/edit_transaction.html",
        {"form":form}) 

def receipt_profile(request, id):
    receipt = models.Receipt.objects.get(id=id)  
    return render(request, "wallet/receipt_profile.html", 
    {"receipt":receipt})         

def edit_receipt(request, id):
    receipt = models.Receipt. objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerReceiptForm(request.POST,
        instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile", id=receipt.id)
    else:
        form = forms.CustomerReceiptForm(instance=receipt)
        return render(request, "wallet/edit_receipt.html",
        {"form":form})                                                 