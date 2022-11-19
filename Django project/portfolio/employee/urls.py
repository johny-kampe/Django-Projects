from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee),
    path('new/', views.employeeNew),
    path('profile/', views.profile, name='profile')
]
