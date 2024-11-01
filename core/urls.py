
from django.urls import path, include
from . import views

app_name = 'HRMS'

urlpatterns = [
    path('', views.index, name="home"),
    path('employees/', views.employees_view, name="employees_view"),
    path('employee/<int:sap_id>/', views.employee_detail_view, name='employee_detail'),
]
