# Generated by Django 4.2.17 on 2025-01-04 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_diff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='user_name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AlterField(
            model_name='timeentry',
            name='time_difference',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timeentry',
            name='user_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]