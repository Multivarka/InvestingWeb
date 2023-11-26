
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))


class SetPasswordFrom(SetPasswordForm):
    new_password1 = forms.CharField(label="новый пароль",widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Повтор пароля',widget=forms.PasswordInput())
    # class Meta:
    #     model = User
    #     fields = ('new_password1', 'new_password2')
        # help_texts = {
        #     'new_password1': None,
        #     'new_password2': None,
        # }
# class PasswordResetingForm(PasswordResetForm):
#
#     class Meta:
#         model = User
#         fields = ('new_password1', 'new_password2')
#         help_texts = {
#             'new_password1': None,
#             'new_password2': None,
#         }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text=None)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput, help_text=None)
    class Meta:
        model = User
        fields = ('username', 'email')
        help_texts = {
            'username': None,
            'email': None,
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


