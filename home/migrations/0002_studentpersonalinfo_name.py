# Generated by Django 4.2.3 on 2023-12-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpersonalinfo',
            name='name',
            field=models.CharField(default='Name', max_length=50),
            preserve_default=False,
        ),
    ]
