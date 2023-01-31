from django.urls import path
from .views import *

urlpatterns = [
	path('create-account/', signup, name='signup'),
	path('', landing, name='landing'),
	path('login/', login, name='login'),
	path('reset-password/', reset_password, name='reset-password'),
	path('forgot-password/', forgot_password, name='forgot-password'),
	path('employee/', employee, name='employee'),
	path('employee_reg/', employee_form, name='employee_form'),
]