# Generated by Django 4.1.6 on 2023-02-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
