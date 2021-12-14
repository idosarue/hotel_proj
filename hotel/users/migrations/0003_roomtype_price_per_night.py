# Generated by Django 4.0 on 2021-12-14 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customer_customerprice_roomprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='price_per_night',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.roomprice'),
        ),
    ]