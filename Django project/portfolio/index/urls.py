from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Being-In-About-Page-Is-Perfect/', views.aboutus, name='about')
]
