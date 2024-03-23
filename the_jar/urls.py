from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home),
    path("user_home", views.user_home, name="user_home"),
    path("logout", views.logout_view),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
