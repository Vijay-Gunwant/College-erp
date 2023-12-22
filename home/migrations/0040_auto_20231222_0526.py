# Generated by Django 3.1.1 on 2023-12-21 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20231222_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='admitcard',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.studentinfo', unique=True),
        ),
    ]
