# Generated by Django 2.1.1 on 2018-09-26 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverlfyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
    ]
