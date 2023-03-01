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
from learn_notes import views

urlpatterns = [
    path('learn/list/', views.learn_list),
    path('learn/list_all/', views.learn_list_all),
    path('learn/del/<int:uid>', views.learn_del),
    path('learn/edit/<int:uid>', views.learn_edit),
    path('learn/add/', views.learn_add),
    path('learn/read/<int:uid>', views.learn_read),

]
