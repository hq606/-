"""tk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import re_path,path
from api import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    #path('api/', views.add_user),
    path('api/login_v1/', views.login_v1),#学生登陆接口
    path('api/login_v2/', views.login_v2),#教师登陆接口
    path('api/add_v1/', views.add_student),#注册学生接口
    path('api/add_v2/', views.add_teacher),#注册教书接口
    path('api/list_v1/', views.list_v1),#学生列表
    path('api/list_v2/', views.list_v2),#教师列表
    path('api/logout/', views.logout),  # 退出
    # path('api/orm/', views.orm),


]
from api.views  import *
from api.courses  import *
from api.class_s import *
urlpatterns+=[

    path('api/question/', QuestionApi.as_view()),
    re_path('api/question/(?P<question_id>\d+)/', QuestionApi.as_view()),

    path('api/course/', CourseApi.as_view()),
    re_path('api/course/(?P<course_id>\d+)/', CourseApi.as_view()),

    path('api/class/', ClassApi.as_view()),
    re_path('api/class/(?P<class_id>\d+)/', ClassApi.as_view()),
]

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register("question_api",views.QuestionView)
# urlpatterns+=router.urls