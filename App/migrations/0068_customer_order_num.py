# Generated by Django 4.2.3 on 2024-06-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0067_remove_customer_order_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='order_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]