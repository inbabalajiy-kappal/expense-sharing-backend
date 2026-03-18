from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from expenses.serializers import ExpenseSerializer
from expenses.services.expense_service import ExpenseService


class ExpenseListCreateView(APIView):

    def __init__(self, service=None, **kwargs):

        super().__init__(**kwargs)
        self.service = service or ExpenseService()

    def get(self, request):

        expenses = self.service.get_all_expenses()

        return Response(expenses, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ExpenseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        expense = self.service.add_expense(
            **serializer.validated_data
        )

        return Response(
            {"id": expense.id},
            status=status.HTTP_201_CREATED
        )


class BalanceListView(APIView):

    def __init__(self, service=None, **kwargs):

        super().__init__(**kwargs)
        self.service = service or ExpenseService()

    def get(self, request):

        balances = self.service.get_all_balances()

        return Response(
            balances,
            status=status.HTTP_200_OK
        )


class HealthCheckView(APIView):

    def get(self, request):

        return Response(
            {
                "status": "healthy",
                "service": "expense-backend"
            },
            status=status.HTTP_200_OK
        )