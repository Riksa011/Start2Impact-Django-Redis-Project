from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # home page
    path('', homepage, name='homepage'),
    # user actions
    path('items-list/', items_list, name='items_list'),
    path('search-item/', search_item, name='search_item'),
    # admin authentication
    path('admin-register/', admin_register, name='admin_register'),
    path('accounts/profile/', admin_profile_view, name='admin_profile_view'),
    path('admin-login/', auth_views.LoginView.as_view(template_name='Progetto/admin_authentication/login.html'), name='admin_login'),
    path('admin-logout/', auth_views.LogoutView.as_view(template_name='Progetto/admin_authentication/logout.html'), name='admin_logout'),
    # admin actions
    path('upload-item/', upload_item, name='upload_item'),
    path('change-item-owner/', change_item_owner, name='change_item_owner'),
]
