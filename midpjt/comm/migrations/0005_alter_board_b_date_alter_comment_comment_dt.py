# Generated by Django 4.0.2 on 2022-03-03 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0004_alter_board_b_date_alter_comment_comment_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 17, 58, 3, 490156)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 17, 58, 3, 490156), null=True),
        ),
    ]
