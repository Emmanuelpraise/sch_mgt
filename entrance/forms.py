from django import forms


class login_form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class employee_form(forms.Form):
    name = forms.CharField(max_length=50)
    salary = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
