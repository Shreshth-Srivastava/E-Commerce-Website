# Generated by Django 4.2.3 on 2024-05-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0043_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
