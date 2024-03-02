from os import getlogin

from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from .views import*


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello1/',hello1,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('hey/',travelpackage,name='travelpackage123'),
    path('print',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('getdate/',getdate,name='getdate'),
    path('DateTime/',DateTime,name='DateTime'),
    path('Sindhuloginfunction/',Sindhuloginfunction,name='Sindhuloginfunction'),
    path('getPieChart/',getPieChart,name='getPieChart'),
    path('PieChart/',PieChart,name='PieChart'),
    path('getCar/', getCar, name='getCar'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('signup/',signup,name='signup'),
    path('signup1/',signup1,name='signup1'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('Feedbackcall/',Feedbackcall, name='Feedbackcall'),
    path('Feedback/',Feedback, name='Feedback'),

]
