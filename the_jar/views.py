from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model

from the_jar.models import Jar


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
    class JarForm(forms.ModelForm):
        class Meta:
            model = Jar
            fields = ('name', 'mode', 'start_date', 'end_date', 'reward', 'punishment')
            widgets = {
                'end_date': forms.DateInput(attrs={'type': 'date'}),
                'start_date': forms.DateInput(attrs={'type': 'date'})
            }

    """
    need to conditionally display fields based on mode - maybe multi-step form?
    """

    if request.method == 'POST':
        form = JarForm(request.POST)
        if form.is_valid():
            jar = form.save()
            jar.users_in_jar.add(request.user)
            jar.save()
            return redirect('/user_home')
    else:
        form = JarForm()
    return render(request, "the_jar/create_jar.html", {'form': form})

def view_jar(request):
    return
