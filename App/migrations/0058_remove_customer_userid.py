# Generated by Django 4.2.3 on 2024-06-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0057_remove_wishlistitem_product_wishlistitem_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='userID',
        ),
    ]
