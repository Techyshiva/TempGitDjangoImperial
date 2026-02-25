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
    path('custom-admin/testimonials/', views.admin_testimonials, name='admin_testimonials'),
    path('custom-admin/testimonials/edit/<int:pk>/', views.admin_testimonials, name='edit_testimonial'),
    path('custom-admin/testimonials/delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
    path('custom-admin/bookings/', views.admin_bookings, name='admin_booking'),
    path('custom-admin/bookings/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('custom-admin/inquiry/', views.admin_inquiry, name='admin_inquiry'),
    path('custom-admin/inquiry/delete/<int:pk>/', views.delete_inquiry, name='delete_inquiry'),
    
]
