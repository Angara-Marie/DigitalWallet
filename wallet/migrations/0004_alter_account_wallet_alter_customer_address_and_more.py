# Generated by Django 4.0.6 on 2022-09-09 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_customer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_account', to='wallet.wallet'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
