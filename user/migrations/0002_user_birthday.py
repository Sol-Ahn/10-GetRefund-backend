# Generated by Django 3.0.8 on 2020-08-04 00:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2020, 8, 4, 0, 3, 35, 63029, tzinfo=utc)),
            preserve_default=False,
        ),
    ]