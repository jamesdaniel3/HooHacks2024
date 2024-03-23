from django.shortcuts import render


def home(request):
    return render(request, 'the_jar/home.html')
