# Generated by Django 3.0.7 on 2020-06-09 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 11, 22, 53, 168156), null=True),
        ),
    ]