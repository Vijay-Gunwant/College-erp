# Generated by Django 3.1.1 on 2023-12-21 01:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20231220_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
