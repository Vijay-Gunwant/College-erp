# Generated by Django 3.1.1 on 2023-12-21 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_admitcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admitcard',
            name='id',
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.studentinfo'),
        ),
    ]
