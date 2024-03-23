from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model


def home(request):
    if request.user.is_authenticated:
        return redirect('/user_home')
    return render(request, 'the_jar/home.html')



def logout_view(request):
    logout(request)
    return redirect("/")

def user_home(request):
    return render(request, 'the_jar/user_home.html')


