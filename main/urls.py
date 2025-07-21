from django.urls import path
from . import views

urlpatterns = [
    path("update/", views.update_status, name="update_status"),
    path("", views.home_status, name="home_status"),
]