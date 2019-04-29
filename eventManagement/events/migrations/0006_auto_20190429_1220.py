# Generated by Django 2.1.7 on 2019-04-29 12:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190429_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 12, 20, 9, 512380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_archive',
            name='ev_start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 12, 20, 9, 513615, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 12, 20, 9, 514965, tzinfo=utc)),
        ),
    ]
