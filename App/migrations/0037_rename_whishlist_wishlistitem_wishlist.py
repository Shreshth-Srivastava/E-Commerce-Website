# Generated by Django 4.2.3 on 2024-05-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0036_rename_whislist_wishlistitem_whishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistitem',
            old_name='whishlist',
            new_name='wishlist',
        ),
    ]