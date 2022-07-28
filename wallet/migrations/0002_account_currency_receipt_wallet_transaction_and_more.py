# Generated by Django 4.0.6 on 2022-07-28 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=10)),
                ('balance', models.IntegerField()),
                ('account_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_of_origin', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('symbol', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=10)),
                ('receipt_date', models.DateTimeField()),
                ('receipt_file', models.FileField(upload_to='')),
                ('total_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
                ('pin', models.IntegerField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_currency', to='wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_REF', models.CharField(max_length=20)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_number', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=10)),
                ('transaction_charge', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_destination', to='wallet.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_origin', to='wallet.account')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_receipt', to='wallet.receipt')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('transaction_cost', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_party_account', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_party_currency', to='wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_reward', models.DateTimeField()),
                ('points', models.IntegerField()),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_wallet', to='wallet.wallet')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_transaction', to='wallet.transaction'),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('recepient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_recepient', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.IntegerField()),
                ('loan_type', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('name', models.CharField(max_length=15)),
                ('loan_status', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('interest_rate', models.IntegerField()),
                ('payment_due_date', models.DateTimeField()),
                ('loan_balance', models.IntegerField()),
                ('guarantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_customer', to='wallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('card_name', models.CharField(max_length=15)),
                ('date_issued', models.DateTimeField()),
                ('card_type', models.CharField(max_length=10)),
                ('expiry_date', models.DateTimeField()),
                ('cvv', models.IntegerField()),
                ('issuer', models.CharField(max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_wallet', to='wallet.wallet'),
        ),
    ]
