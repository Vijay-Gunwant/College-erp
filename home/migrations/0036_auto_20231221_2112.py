# Generated by Django 3.1.1 on 2023-12-21 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_result_backlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='resultEnd',
            new_name='file',
        ),
    ]
