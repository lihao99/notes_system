"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.db import router
from django.urls import path
from app01 import views

urlpatterns = [
    path('user/list/', views.user_list),
    path('admin/register/', views.admin_register),
    path('user/add/', views.user_add),
    path('user/edit/<int:uid>', views.user_edit),
    path('user/del/<int:uid>', views.user_del),
    path('login/', views.login),
    path('logout/', views.logout),
    path('images/code/', views.images_code),
    path('test/', views.test),
    path('count/num/', views.count_num),
    path('chart/bar/',views.chart_bar),
    path('update/',views.update_pi)

]
