# Generated by Django 2.1.7 on 2019-05-01 00:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20190430_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 0, 1, 34, 117678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_archive',
            name='ev_start_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 0, 1, 34, 119080, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 0, 1, 34, 120779, tzinfo=utc)),
        ),
    ]
