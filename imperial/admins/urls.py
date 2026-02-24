from django.urls import path, include
from admins import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),

]
