from django.urls import path
from .views import ExpenseListCreateView, BalanceListView, HealthCheckView


urlpatterns = [
    path('api/expenses/', ExpenseListCreateView.as_view()),
    path('api/balances/', BalanceListView.as_view()),
    path('health/', HealthCheckView.as_view()),
]