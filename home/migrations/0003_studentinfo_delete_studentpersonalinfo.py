# Generated by Django 4.2.3 on 2023-12-16 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_studentpersonalinfo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('studentId', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('emailCollege', models.EmailField(max_length=254)),
                ('emailPersonal', models.EmailField(max_length=254)),
                ('registerDate', models.DateField(default=datetime.date(2023, 12, 16))),
                ('mobileNo', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='StudentPersonalInfo',
        ),
    ]