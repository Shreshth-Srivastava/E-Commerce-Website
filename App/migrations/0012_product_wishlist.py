# Generated by Django 5.0.1 on 2024-03-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_rename_counter_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.BooleanField(default=False),
        ),
    ]
