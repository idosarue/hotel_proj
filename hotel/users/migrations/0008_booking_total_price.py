# Generated by Django 3.2.6 on 2022-01-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220116_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
