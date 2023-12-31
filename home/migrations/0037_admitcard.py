# Generated by Django 3.1.1 on 2023-12-21 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20231221_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmitCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('back_file', models.FileField(default=None, upload_to='resultEnd/')),
                ('normal_file', models.FileField(default=None, upload_to='resultEnd/')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.studentinfo')),
            ],
        ),
    ]
