from django.urls import path
from .views import ExpenseListCreateView,BalanceListView,HealthCheckView
urlpatterns = [
    path('api/expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('api/balances/', BalanceListView.as_view(), name='balance-list'),
    path("health/", HealthCheckView.as_view(), name="health-check"),
]