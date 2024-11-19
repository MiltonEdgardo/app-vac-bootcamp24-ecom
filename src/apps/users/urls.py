from django.urls import path
from . import views


app_name = "users"
urlpatterns = [

    path('list/', views.users_list, name="list"),
]