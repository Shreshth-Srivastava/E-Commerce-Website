# Generated by Django 5.0.1 on 2024-03-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_counter_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='name',
            field=models.CharField(default='Product', max_length=200),
        ),
    ]
