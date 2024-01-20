from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView
from .forms import LoginForm, PasswordChangingForm, UserRegistrationForm, SetPasswordFrom
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import ProductInvest, Category
import requests
from parser import get_cat_info

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("password_success")

def password_success(request):
    return render(request, 'registration/password_change_done.html', {})


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = SetPasswordFrom


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd["username"],
                                password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Успешный вход")
                else:
                    return HttpResponse("Неактивный пользователь")
            else:
                return HttpResponse("Неверный логин")
    else:
        form = LoginForm()
    return render(request, "invest/login.html",
                  {"form": form})

@login_required
def dashboard(request):
    return render(request,
    'invest/dashboard.html',
    {'section': 'dashboard'})


def update_table(category):
    session = requests.Session()
    res = get_cat_info(session, category)
    if not ProductInvest.objects.filter(title=res[0]).exists():
        product = ProductInvest(category=Category.objects.get(slug="currencies"), title=res[0],
                                price_now=round(res[1], 2), price_change=res[2])
        product.save()
    else:
        product = ProductInvest.objects.get(title=res[0])
        product.price_now = round(res[1], 2)
        product.price_change = res[2]
        product.save()
    print(f'{res[0]} - {res[1]}({res[2]})')



@login_required
def table(request, category_slug='currencies'):
    update_table(category_slug)
    category = None
    categories = Category.objects.all()
    products = ProductInvest.objects.all()
    if category_slug:
        category = categories.get(slug=category_slug)
        products = products.filter(category=category)
    print(products)
    return render(request, 'invest/table.html', {'products': products, 'categories': categories, 'category': category})