# Generated by Django 4.2.3 on 2024-05-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0033_remove_wishlist_product_wishlistitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishlistItems',
            new_name='WishlistItem',
        ),
    ]