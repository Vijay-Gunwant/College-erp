# Generated by Django 3.1.1 on 2023-12-21 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20231221_0709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='course_type',
            new_name='courseType',
        ),
    ]
