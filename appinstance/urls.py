"""
URL configuration for appinstance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('administration/', views.administration, name='administration'),
    path('login/', views._login, name='login'),
    path('logout/', views._logout, name='logout'),
    path('register/', views.register, name='register'),
    path('request/', views.request_page, name='request'),
    path('donation/', views.donation, name='donation'),
    path('donation_admin/', views.donation_admin, name='donation_admin'),
    path('procurement_admin/', views.procurement_admin, name='procurement_admin'),
    path('request_admin/', views.request_admin, name='request_admin'),
    path('get_request_details/', views.get_request_details, name='get_request_details'),
    path('get_purchased_items/', views.get_purchased_items, name='get_purchased_items'),
    path('update_request/', views.update_request, name='update_request'),
    path('inventory_admin/', views.inventory_admin, name='inventory_admin'),
    path('reporting_admin/', views.reporting_admin, name='reporting_admin'),
    path('get_donated_items/', views.get_donated_items, name='get_donated_items'),
    path('delete_donation/', views.delete_donation, name='delete_donation')
]