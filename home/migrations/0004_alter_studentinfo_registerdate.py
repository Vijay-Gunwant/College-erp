# Generated by Django 4.2.3 on 2023-12-16 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_studentinfo_delete_studentpersonalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='registerDate',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 4, 31, 6, 506225, tzinfo=datetime.timezone.utc)),
        ),
    ]
