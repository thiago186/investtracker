from django.urls import path, include
from . import views

app_name = 'assets'
urlpatterns = [
    path('', views.home, name='home'),
    path('workingON/', views.workingOn, name='workingOn'),
    path('create_stock/', views.create_stock, name='create_stock'),
    path('investment_funds/', views.create_investment_funds, name='create_investment_funds'),
    path('fixed_income/', views.create_fixed_income, name='create_fixed_income'),
]
