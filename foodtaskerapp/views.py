from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import UserForm, ResturantForm, UserFormEdit, MealForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from foodtaskerapp.models import Meal, Order
# Create your views here.

def home(request):
    return redirect(resturant_home)

@login_required(login_url='/resturant/sign-in/')
def resturant_home(request):
    return redirect(resturant_order)

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



#------------------
@login_required(login_url='/resturant/sign-in/')
def resturant_account(request):
    user_form = UserFormEdit(instance=request.user)
    resturant_form = ResturantForm(instance=request.user.resturant)
    
    if request.method == "POST":
        user_form = UserFormEdit(request.POST, instance=request.user)
        resturant_form = ResturantForm(request.POST, request.FILES, instance=request.user.resturant)

        if user_form.is_valid() and resturant_form.is_valid():
            user_form.save()
            resturant_form.save()

    return render(request, 'resturant/account.html',{
        "user_form":user_form,
        "resturant_form":resturant_form
    })

@login_required(login_url='/resturant/sign-in/')
def resturant_meal(request):
    meals = Meal.objects.filter(resturant=request.user.resturant).order_by('-id')
    
    return render(request, 'resturant/meal.html',{"meals":meals})

@login_required(login_url='/resturant/sign-in/')
def resturant_add_meal(request):
    form = MealForm()

    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.resturant = request.user.resturant
            meal.save()
            return redirect(resturant_meal)

    return render(request, 'resturant/add_meal.html',{
        "form":form,
    })


@login_required(login_url='/resturant/sign-in/')
def resturant_edit_meal(request, meal_id):
    form = MealForm(instance=Meal.objects.get(id=meal_id))

    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES, instance=Meal.objects.get(id=meal_id))

        if form.is_valid():
            form.save()
            return redirect(resturant_meal)

    return render(request, 'resturant/add_meal.html',{
        "form":form,
    })



@login_required(login_url='/resturant/sign-in/')
def resturant_order(request):
    orders = Order.objects.filter(resturant=request.user.resturant).order_by('-id')
    return render(request, 'resturant/order.html',{"orders":orders})

@login_required(login_url='/resturant/sign-in/')
def resturant_report(request):
    return render(request, 'resturant/report.html',{})