from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('add/', views.add_transaction, name = 'add_transactions'),
    path('show_list/', views.get_transactions, name = 'transactions_list'),
    path('login/', views.user_login, name = 'login'),
    path('registration/', views.registration, name = 'registration'),
    path('add_category/', views.add_category, name = 'add_category'),
    path('filtered_transactions/', views.filtered_transactions, name = 'filtered_transactions'),
    path('logout/',views.logout, name = 'logout')
    
]
