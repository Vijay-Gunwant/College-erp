# Generated by Django 4.2.3 on 2023-12-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_studentinfo_registerdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='course',
            field=models.CharField(default='hg', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='specialization',
            field=models.CharField(default='hg', max_length=50),
            preserve_default=False,
        ),
    ]