from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordChangeView, PasswordResetConfirmView


urlpatterns = [
    # path("login/", views.user_login, name="login")
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('table/', views.table, name="table"),
    path('table/<category_slug>', views.table, name="update-table"),
    path('', include('django.contrib.auth.urls')),
]