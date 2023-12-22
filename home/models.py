import datetime

from django.db import models
from django.forms import forms
from django.utils import timezone


# Create your models here.
class StudentInfo(models.Model):
    studentId = models.IntegerField(primary_key=True)
    password = models.CharField(null=False, max_length=10)
    name = models.CharField(null=False, max_length=50)
    gender = models.CharField(null=False, max_length=10)
    emailCollege = models.EmailField(null=False)
    emailPersonal = models.EmailField(null=False)
    registerDate = models.DateField(default=timezone.now)
    mobileNo = models.BigIntegerField(null=False)
    courseId = models.CharField(null=False, max_length=10)
    college_campus = models.CharField(max_length=100, null=False, default="GEHU-HLD")
    university = models.CharField(max_length=100, null=False, default="Graphic Era Hill University")
    studentType = models.CharField(max_length=50, default="Regular")
    section = models.CharField(max_length=5, default="A")
    feeFrequency = models.CharField(max_length=30, default="Half-Yearly")

    def __str__(self):
        return str(self.studentId)


class StudentPersonalInfo(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    fatherName = models.CharField(max_length=100, null=False)
    motherName = models.CharField(max_length=100, null=False)
    bloodGroup = models.CharField(max_length=5, default="N/A")
    category = models.CharField(max_length=10, default="N/A")
    profileImg = models.ImageField(upload_to='profileImages/', default="profileImages/profile.png")
    current_address = models.CharField(max_length=100, default="")
    permanent_address = models.CharField(max_length=100, default="")
    dob = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return str(self.studentId)


class StudentEducationInfo(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    instituteName_10 = models.CharField(max_length=100, null=False)
    board_10 = models.CharField(max_length=50, null=False)
    markSheet_10 = models.ImageField(upload_to='markSheet10/', null=False)
    percent_10 = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    passOutYear_10 = models.CharField(max_length=4, null=False)
    instituteName_12 = models.CharField(max_length=100, null=False)
    board_12 = models.CharField(max_length=50, null=False)
    markSheet_12 = models.ImageField(upload_to='markSheet12/', null=False)
    percent_12 = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    passOutYear_12 = models.CharField(max_length=4, null=False)
    tc_migration = models.ImageField(upload_to='tcMigrations/', null=False, default="")

    def __str__(self):
        return str(self.studentId)


class FeeDetails(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    sem = models.IntegerField()
    feeName = models.CharField(max_length=50)
    dues = models.DecimalField(decimal_places=2, max_digits=10)
    scholarship = models.DecimalField(decimal_places=2, max_digits=10)
    paid = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.studentId) + str(self.feeName)


class FeeReceipt(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    sem = models.IntegerField()
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    feeReceipt = models.FileField(upload_to="feeReceipt/")
    feeDescription = models.CharField(max_length=200)

    def __str__(self):
        return str(self.studentId) + "_" + str(self.sem)


class Courses(models.Model):
    courseId = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=100, default="")
    specialization = models.CharField(max_length=50, default="N/A")
    sem = models.IntegerField()
    timetable = models.FileField(upload_to='timetable/', null=False, default="")
    courseType = models.CharField(max_length=50, null=False, default="UG")

    def __str__(self):
        return self.courseId


class SubjectsInfo(models.Model):
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    subjectId = models.CharField(primary_key=True, max_length=10)
    subjectName = models.CharField(max_length=100)
    syllabus = models.FileField(upload_to="syllabus/", default="")
    teacherName = models.CharField(max_length=100)
    teacherImg = models.ImageField(upload_to="teacherProfileImg/", default="profileImages/profile.png")

    def __str__(self):
        return self.subjectId


class Circular(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to="circular/")
    issuedBy = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Notification(models.Model):
    description = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to="notification/")
    issuedBy = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Events(models.Model):
    eventName = models.CharField(max_length=500)
    dateTo = models.DateField(default=timezone.now)
    dateFrom = models.DateField(default=timezone.now)
    file = models.FileField(upload_to="notification/")
    link = models.CharField(max_length=1000)
    issuedBy = models.CharField(max_length=100)

    def __str__(self):
        return self.eventName


class Result(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    sem = models.IntegerField()
    type = models.CharField(max_length=5)
    file = models.FileField(upload_to="resultEnd/", default="None")
    backlog = models.CharField(max_length=50)

    def __str__(self):
        return str(self.studentId) + "_" + str(self.sem)


class AdmitCard(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    sem = models.IntegerField()
    back_file = models.FileField(upload_to="resultEnd/", default="None")
    normal_file = models.FileField(upload_to="resultEnd/", default="None")

    def __str__(self):
        return str(self.studentId) + "_" + str(self.sem)


class Attendance(models.Model):
    studentId = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    month = models.IntegerField()
    day = models.IntegerField()
    year = models.CharField(max_length=4,default="")
    status = models.CharField(max_length=10,
                              choices=[("Absent", "Absent"), ("Present", "Present"), ("No Class", "No Class")],
                              default="No Class")

    def __str__(self):
        return self.year + "_" + str(self.month)+"_"+str(self.day)
