from django.shortcuts import render, redirect


def home(request):
    return render(request, 'the_jar/home.html')


def logout_view(request):
    logout(request)
    return redirect("/")


