# Generated by Django 4.0.2 on 2022-03-07 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 8, 8, 55, 43, 8211)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 8, 8, 55, 43, 8211), null=True),
        ),
    ]
