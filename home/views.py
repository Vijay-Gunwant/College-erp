from datetime import date

from django.forms import forms
from django.shortcuts import render, HttpResponse
from home.models import *


def image_validation(image):
    width, height = image.width, image.height
    max_width = 512
    max_height = 512

    if width > max_width or height > max_height:
        raise forms.ValidationError("Image dimensions should be within 512x512 pixels. Please resize you image using "
                                    "a Image resizer!!!")


# Create your views here.
def login(request):
    context = {
        "message": "Welcome Student!!!"
    }
    if request.method == "POST":
        studentId = request.POST.get('StudentID')
        password = request.POST.get('Password')

        try:
            obj = StudentInfo.objects.get(studentId=studentId, password=password)
            request.session['studentId'] = studentId
            return home(request)
        except:
            context = {
                "message": "Invalid Credentials!!!!"
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html', context)


def forgot(request):
    context = {
        "message": "Welcome Student!!!"
    }

    if request.method == "POST":
        studentId = request.POST.get("StudentId")
        email = request.POST.get("Email")
        try:
            obj = StudentInfo.objects.get(studentId=studentId, emailPersonal=email)
            request.session['studentId'] = studentId
            context["message"] = "Please Change Your Password"
            return render(request, 'reset.html', context)
        except:
            context["message"] = "Details don't match/exists!"

    return render(request, 'forgot.html', context)


def reset(request):
    context = {
        "message": "Welcome Student!!!"
    }
    if request.method == "POST":
        password = request.POST.get("Password")
        confirm = request.POST.get("Confirm")
        print(password, confirm)
        try:
            studentId = request.session["studentId"]
        except:
            context["message"] = "Please first enter details here!!"
            return render(request, 'forgot.html', context)
        if len(password) < 8:
            context["message"] = "Password should have length 8 or more!!"
        elif password != confirm:
            context["message"] = "Password and Confirm Password don't match!!"
        else:
            try:
                StudentInfo.objects.filter(studentId=studentId).update(password=password)

                context["message"] = "Password is Changed Successfully!!!"
                return render(request, 'login.html', context)
            except:
                context["message"] = "PLease restart the process!!"
    return render(request, 'reset.html', context)


def home(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})

    studentInfo = StudentInfo.objects.get(studentId=studentId)
    courseId = studentInfo.courseId
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    EducationInfo = StudentEducationInfo.objects.get(studentId=studentId)
    courseInfo = Courses.objects.get(courseId=courseId)
    subjectInfo = list(SubjectsInfo.objects.filter(courseId=courseId))

    context = {
        "studentId": studentId,
        "fname": studentInfo.name.split()[0],
        "name": studentInfo.name,
        "mobileNo": studentInfo.mobileNo,
        "email": studentInfo.emailPersonal,
        "profileImg": personalInfo.profileImg,
        "father": personalInfo.fatherName,
        "mother": personalInfo.motherName,
        "dob": personalInfo.dob,
        "bloodGroup": personalInfo.bloodGroup,
        "percent10": EducationInfo.percent_10,
        "percent12": EducationInfo.percent_12,
        "studentType": studentInfo.studentType,
        "courseType": courseInfo.courseType,
        "course": courseInfo.courseName.title(),
        "university": studentInfo.university.title(),
        "branch": courseInfo.specialization,
        "college": studentInfo.college_campus,
        "section": studentInfo.section,
        "sem": courseInfo.sem,
        "marksheet10": EducationInfo.markSheet_10,
        "marksheet12": EducationInfo.markSheet_12,
        "timetable": courseInfo.timetable,
        "subjectInfo": subjectInfo
    }

    return render(request, 'home.html', context)


def fees(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    courseId = studentInfo.courseId
    courseInfo = Courses.objects.get(courseId=courseId)
    feeDetails = FeeDetails.objects.filter(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    dues = 0
    scholarship = 0
    paidAmount = 0
    balance = 0

    for i in feeDetails:
        dues += i.dues
        scholarship += i.scholarship
        paidAmount += i.paid
        balance += i.balance

    context = {
        "fname": studentInfo.name.split()[0],
        "name": studentInfo.name,
        "profileImg": personalInfo.profileImg,
        "studentId": studentId,
        "course": courseInfo.courseName,
        "sem": courseInfo.sem,
        "feeDetails": list(feeDetails),
        "date": str(date.today()),
        "dues": dues,
        "scholarship": scholarship,
        "paid": paidAmount,
        "balance": balance,
        "feeFreq": studentInfo.feeFrequency

    }
    return render(request, 'feesSubmission.html', context)


def choose_fees(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
    }
    return render(request, 'fees.html', context)


def feeReceipt(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    Receipt = list(FeeReceipt.objects.filter(studentId=studentId))
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
        "receipt": Receipt
    }
    return render(request, 'feeReceipt.html', context)


def circular(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    temp = list(Circular.objects.all())
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
        "temp": temp
    }
    return render(request, 'circular.html', context)


def notification(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    temp = list(Notification.objects.all())
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
        "temp": temp
    }
    return render(request, 'notification.html', context)


def temp(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
    }
    return render(request, 'temp.html', context)


def events(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    temp = list(Events.objects.all())
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
        "temp": temp
    }
    return render(request, 'events.html', context)


def choose_exams(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
    }
    return render(request, 'exams.html', context)


def result(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)

    Res = list(Result.objects.filter(studentId=studentId))
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
        "Res": Res
    }
    return render(request, 'result.html', context)


def Admit_Card(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    admit_card = AdmitCard.objects.get(studentId=studentId)

    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
        "normal": admit_card.normal_file,
        "back": admit_card.back_file,

    }
    return render(request, 'AdmitCard.html', context)


def academics(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)

    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,

    }
    return render(request, 'academics.html', context)


def tracker(request):
    try:
        studentId = request.session['studentId']
    except:
        return render(request, 'login.html', {"message": "Please Login First!!!"})
    studentInfo = StudentInfo.objects.get(studentId=studentId)
    personalInfo = StudentPersonalInfo.objects.get(studentId=studentId)
    context = {
        "fname": studentInfo.name.split()[0],
        "profileImg": personalInfo.profileImg,
    }
    if request.method == "POST":
        year = request.POST.get("year")
        month = request.POST.get("month")
        print(year + " " + month)
        attendance_details = list[Attendance.objects.filter(studentId=studentId, month=month, year=year)]
        context["attendance_details"] = attendance_details
    print(context)
    return render(request, 'tracker.html', context)
