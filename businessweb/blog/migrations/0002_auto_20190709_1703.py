# Generated by Django 2.2.2 on 2019-07-09 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 17, 3, 30, 876624, tzinfo=utc), verbose_name='Publication date'),
        ),
    ]
