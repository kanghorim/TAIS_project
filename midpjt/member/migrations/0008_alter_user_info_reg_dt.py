# Generated by Django 4.0.2 on 2022-03-03 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_alter_user_info_reg_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='reg_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 17, 58, 3, 489158)),
        ),
    ]