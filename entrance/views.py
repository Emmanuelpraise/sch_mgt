from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from entrance.models import Employee

from .forms import *


# Create your views here.
def signup(request):
    template = loader.get_template("sign_up.html")
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template("login.html")
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            print(form.cleaned_data['password'])
        return HttpResponse(template.render({'form': form}, request))
    else:
        form = login_form()
        return HttpResponse(template.render({'form': form}, request))


def employee(request):
    template = loader.get_template("employee.html")
    if request.method == 'POST':
        form = employee_form(request.POST)
        return HttpResponse(template.render({'form': form}, request))
    else:
        form = employee_form()
        return HttpResponse(template.render({'form': form}, request))


def forgot_password(request):
    template = loader.get_template("forgot_pwd.html")
    return HttpResponse(template.render())


def reset_password(request):
    template = loader.get_template("reset_pwd.html")
    return HttpResponse(template.render())


def landing(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def get_data():
    return [
    {'firstname':'Praise', 'lastname':'Ayelabola', 'phone':'09139268581', 'email':'emmanuelpraise36@gmail.com', 'department':'engineering', 'salary':400000, 'employment_date':'2023-01-01'}
    ]


def employee_form(request):
    employees = Employee.objects.all()

    method = request.method
    print('Method....', method)
    if method == 'GET':
        template = loader.get_template("employee_form.html")
        options = {'login_option': ['Admin', 'Account', 'Sales']}
        return HttpResponse(template.render({'data':get_data(), 'message':'Data Retrived!', 'employees': employees}, request))
    else:
        print('You clicked Submit')
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        department = request.POST['department']
        salary = float(request.POST['salary'])
        employment_date = datetime.strptime(request.POST['employment_date'], '%Y-%m-%d')
        print(f'You posted Firstname: {firstname}, lastname: {lastname}, phone: {phone}, email: {email}, department: {department}, salary: {salary}, employment_date: {employment_date}')
        employee = Employee.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], phone=request.POST['phone'], email=request.POST['email'], department=request.POST['department'], salary=salary, employment_date=employment_date)
        return render(request, 'employee_form.html', {'data':get_data(), 'message':'Registration Successful!', 'employees': employees})
