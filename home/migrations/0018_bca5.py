# Generated by Django 3.1.1 on 2023-12-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20231221_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='BCA5',
            fields=[
                ('subjectId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subjectName', models.CharField(max_length=100)),
                ('syllabus', models.FileField(default='', upload_to='syllabus/')),
                ('teacherName', models.CharField(max_length=100)),
                ('teacherImg', models.FileField(default='profileImages/profile.png', upload_to='teacherProfileImg/')),
            ],
        ),
    ]
