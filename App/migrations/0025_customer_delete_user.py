# Generated by Django 4.2.3 on 2024-05-23 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0024_alter_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('username', models.CharField(default='User', max_length=200)),
                ('password', models.CharField(default=None, max_length=15, null=True)),
                ('cart', models.IntegerField(default=0)),
                ('orderPrice', models.IntegerField(default=0)),
                ('wishlist', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
