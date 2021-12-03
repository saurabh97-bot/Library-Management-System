"""LibMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('',Homepage.as_view()),
    path('nav',Navbr.as_view()),
    path('book',BookList.as_view()),
    path('issue',BookIssueRecords.as_view()),
    path('issueform',BookIssue.as_view()),
    path('student',StudentDetail.as_view()),
    path('add',AddBooks.as_view()),
    path('add-stud',AddStudent.as_view()),
    path('update-student/<str:pk>',UpdateStudent.as_view()),
    path('update-book/<str:pk>',UpdateBooks.as_view()),
    path('delete-student/<str:pk>',DeleteStudent.as_view()),
    path('delete-book/<str:pk>',DeleteBooks.as_view()),
    path('signup',registeradmin),
    path('logpage',loginpage)
]
