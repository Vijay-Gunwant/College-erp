# Generated by Django 3.1.1 on 2023-12-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20231221_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='id',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='section',
            field=models.CharField(default='A', max_length=5),
        ),
        migrations.AlterField(
            model_name='courses',
            name='courseId',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
    ]