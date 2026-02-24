from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('portfolio/', views.admin_portfolio, name='admin_portfolio'),
    path('portfolio/edit/<int:pk>/', views.admin_portfolio, name='edit_portfolio'),
    path('custom-admin/portfolio/delete/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),
    path('custom-admin/gallery/', views.admin_gallery, name='admin_gallery'),
    path('custom-admin/gallery/edit/<int:pk>/', views.admin_gallery, name='edit_gallery'),
    path('custom-admin/gallery/delete/<int:pk>/', views.delete_gallery, name='delete_gallery'),
    path('admin/team/', views.team_admin, name='team_admin'),
    path('admin/team/edit/<int:pk>/', views.edit_team, name='edit_team'),
    path('admin/team/delete/<int:pk>/', views.delete_team, name='delete_team'),
    path('custom-admin/careers/', views.admin_careers, name='admin_careers'),
    path('custom-admin/careers/edit/<int:pk>/', views.admin_careers, name='edit_job'),
    path('custom-admin/careers/delete/<int:pk>/', views.delete_job, name='delete_job'),
    
]
