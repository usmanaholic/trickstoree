# Generated by Django 5.1.3 on 2024-11-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='recent',
            field=models.BooleanField(default=False),
        ),
    ]
