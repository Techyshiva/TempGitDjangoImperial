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
    path('custom-admin/featured/', views.manage_featured, name='manage_featured'),
    path('custom-admin/featured/edit/<int:pk>/', views.manage_featured, name='edit_featured'),
    path('custom-admin/featured/delete/<int:pk>/', views.delete_featured, name='delete_featured'),
    path('custom-admin/featured/', views.manage_featured, name='manage_featured'),
    path('custom-admin/featured/edit/<int:pk>/', views.manage_featured, name='edit_featured'),
    path('custom-admin/featured/delete/<int:pk>/', views.delete_featured, name='delete_featured'),
    
]
