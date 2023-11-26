from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView
from .forms import LoginForm, PasswordChangingForm, UserRegistrationForm, SetPasswordFrom
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import ProductInvest, Category
import requests
import apimoex

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


def update_table():
    with requests.Session() as session:
        securities = [sec['SECID'] for sec in apimoex.get_board_securities(session)][:10]
        for security in securities:
            data = apimoex.get_board_history(session, security)[-2:]
            volume1, value1 = data[-1]['VOLUME'], data[-1]['VALUE']
            volume2, value2 = data[0]['VOLUME'], data[0]['VALUE']
            perc = '+100%'
            if volume1 > 0:
                price = value1 / volume1
                if volume2 > 0:
                    price2 = value2 / volume2
                    perc = round((price - price2) / price2 * 100, 2)
                    res = f'+{perc}%' if perc > 0 else f'{perc}%'
                    if not ProductInvest.objects.filter(title=security).exists():
                        product = ProductInvest(category=Category.objects.get(slug="forex"), title=security,
                                                price_now=round(price, 2), price_change=res)
                        product.save()
                    else:
                        product = ProductInvest.objects.get(title=security)
                        product.price_now = round(price, 2)
                        product.price_change = res
                        product.save()
                    print(f'{security} - {price}({res})')



@login_required
def table(request, category_slug='forex'):
    # update_table()
    category = None
    categories = Category.objects.all()
    products = ProductInvest.objects.all()
    if category_slug:
        category = categories.get(slug=category_slug)
        products = products.filter(category=category)
    print(products)
    return render(request, 'invest/table.html', {'products': products, 'categories': categories, 'category': category})