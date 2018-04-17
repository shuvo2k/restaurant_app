from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import UserForm, ResturantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return redirect(resturant_home)

@login_required(login_url='/resturant/sign-in/')
def resturant_home(request):
    return render(request, 'resturant/home.html')

def resturant_sign_up(request):
    user_form = UserForm()
    resturant_form = ResturantForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        resturant_form = ResturantForm(request.POST, request.FILES)

    if user_form.is_valid() and resturant_form.is_valid():
        new_user = User.objects.create_user(**user_form.cleaned_data)
        new_resturant = resturant_form.save(commit=False)
        new_resturant.user = new_user
        new_resturant.save()

        login(request, authenticate(
            username = user_form.cleaned_data['username'],
            password = user_form.cleaned_data['password']
        ))

        return redirect(resturant_home)

    return render(request, 'resturant/sign-up.html', {
        'user_form': user_form,
        'resturant_form': resturant_form,
    })