from django.urls import path
from real_state_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
]
