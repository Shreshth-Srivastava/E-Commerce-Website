# Generated by Django 4.2.3 on 2024-05-24 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0037_rename_whishlist_wishlistitem_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
