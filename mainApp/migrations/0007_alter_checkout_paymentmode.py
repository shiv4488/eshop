# Generated by Django 3.2.8 on 2022-11-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='paymentmode',
            field=models.IntegerField(choices=[(1, 'COD'), (2, 'Net Banking')], default=0),
        ),
    ]