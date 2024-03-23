from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home),
    path("user_home", views.user_home, name="user_home"),
    path("create_jar", views.create_jar, name="create_jar"),
    path("view_jar", views.view_jar, name="view_jar"),
    path("logout", views.logout_view),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
