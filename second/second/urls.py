"""second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/',views.index,name='index'),
    path('resume/',include('resume.urls')),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('education/',views.education,name="education"),
    path('deleteedu/',views.deleteedu,name="deleteEdu"),
    path('jobs/', views.jobs, name="jobs"),
    path('deletejob/',views.deletejob,name="deletejob"),
    path('internship/', views.intern, name="internship"),
    path('deleteintern/',views.deleteintern,name="deleteintern"),
    path('training/', views.training, name="training"),
    path('deletetrain/', views.deletetrain, name="deletetrain"),
    path('project/', views.project, name="project"),
    path('deleteproject/', views.deletepro, name="deleteproject"),
    path('skill/', views.skill, name="skill"),
    path('deleteskill/', views.deleteskill, name="deleteskill"),
    path('additional/', views.additional, name="additional"),
    path('deleteadd/', views.deleteadd, name="deleteadd"),
]
