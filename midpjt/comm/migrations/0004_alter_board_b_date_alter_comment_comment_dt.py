# Generated by Django 4.0.2 on 2022-03-03 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0003_alter_board_b_date_alter_comment_comment_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 17, 50, 28, 154314)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 17, 50, 28, 154314), null=True),
        ),
    ]