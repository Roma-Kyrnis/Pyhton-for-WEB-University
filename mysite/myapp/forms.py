from django import forms

class UserForm(forms.Form):
    Email = forms.EmailField(required=False, min_length=7, help_text="Введите свою почту")
    Password = forms.RegexField(r"^[\w@$^*]{8,16}$", help_text="Введите свой пароль")