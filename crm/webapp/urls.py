from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.HomeView.as_view(), name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('client/<int:pk>/', views.client_view, name='client'),
    path('client_delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_update/<int:pk>/', views.client_update, name='client_update'),
]
