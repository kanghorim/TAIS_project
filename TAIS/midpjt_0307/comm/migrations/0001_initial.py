# Generated by Django 4.0.2 on 2022-03-07 01:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_kind', models.CharField(max_length=10)),
                ('board_no', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('b_title', models.CharField(max_length=1000)),
                ('b_content', models.TextField()),
                ('b_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 7, 10, 4, 35, 419027))),
                ('b_count', models.IntegerField(default=1)),
                ('b_group', models.IntegerField(default=0)),
                ('b_step', models.IntegerField(default=0)),
                ('b_indent', models.IntegerField(default=0)),
                ('b_img', models.ImageField(blank=True, upload_to='')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.user_info')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_dt', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 7, 10, 4, 35, 419027), null=True)),
                ('comment_no', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='comm.board')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.user_info')),
            ],
        ),
    ]