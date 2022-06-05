from .views import index, login_view, register, admin, customer, employee
from django.urls import path


urlpatterns=[
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('register/', register, name='register'),
    path('adminpage/', admin, name='adminpage'),
    path('customer/', customer, name='customer'),
    path('employee/', employee, name='employee'),
]