# Generated by Django 3.2.6 on 2022-01-07 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220107_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_finalized',
        ),
    ]