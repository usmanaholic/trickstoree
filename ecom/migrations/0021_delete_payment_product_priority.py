# Generated by Django 5.1.3 on 2024-12-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0020_payment_alter_customer_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='product',
            name='priority',
            field=models.IntegerField(default=100),
        ),
    ]
