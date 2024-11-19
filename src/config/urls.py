"""
URL configuration for appvac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from django.contrib.auth import views as views_django

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', views.home_page, name="home"),
    path('', views.home_page, name="home"),
    #path('login', views.login_page, name="login"),

    path('login', views_django.LoginView.as_view(template_name = "login_page.html"), name="login"),

    path('users/list/', views.users_list, name="users_list"),
    path('patients/list/', views.patients_list, name="patients_list")
]
