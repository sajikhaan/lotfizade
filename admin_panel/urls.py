from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    
    path('service/add/', views.add_service, name='add_service'),
    path('service/<int:pk>/edit/', views.edit_service, name='edit_service'),
    path('service/<int:pk>/delete/', views.delete_service, name='delete_service'),

    path('photo/add/', views.add_photo, name='add_photo'),
    path('photo/<int:pk>/delete/', views.delete_photo, name='delete_photo'),

    path('post/add/', views.add_post, name='add_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]
