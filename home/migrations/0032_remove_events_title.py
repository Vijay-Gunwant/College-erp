# Generated by Django 3.1.1 on 2023-12-21 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_circular_events_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='title',
        ),
    ]
