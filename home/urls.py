from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('forgot',views.forgot,name='forgot'),
    path('reset',views.reset,name='reset'),
    path('home',views.home,name='home'),
    path('circular',views.circular,name='circular'),
    path('notification',views.notification,name='notification'),
    path('events',views.events,name='events'),
    path('feesSubmission',views.fees,name='feesSubmission'),
    path('fees',views.choose_fees,name='fees'),
    path('feeReceipt',views.feeReceipt,name="feeReceipt"),
    path('temp',views.temp,name="temp"),
    path('exam',views.choose_exams,name="exam"),
    path('result',views.result,name="result"),
    path('admitCard',views.Admit_Card,name="admitCard"),
    path('academics',views.academics,name="academics"),
    path('tracker',views.tracker,name="tracker"),
]