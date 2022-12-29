from django.urls import path
from Api_App import views

urlpatterns = [
    path('', views.ExpenseListCreate.as_view(), name='expense-list-create')
    
]