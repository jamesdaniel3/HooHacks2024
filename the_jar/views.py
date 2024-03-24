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

def create_jar(request):
    return

def view_jar(request):
    return

def my_jars(request):

    jars_list = Jars.objects.all()

    jars_list_for_user = []
    for each in jars_list:
        if request.user in each.users:
            jars_list_for_user.append(each)

    return render(request, 'the_jar/my_jars', {'users_in_jar': users_in_jar, 'jars_list': jars_list_for_user})

