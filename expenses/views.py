from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExpenseListCreateView(APIView):

    
    MOCK_EXPENSES = [
        {
            "id": 1,
            "payer_id": 1,
            "amount": 1000.00,
            "split_type": "EQUAL",
            "participants": [1, 2, 3],
            "created_at": "2026-03-05T12:00:00Z"
        },
        {
            "id": 2,
            "payer_id": 2,
            "amount": -500.00,
            "split_type": "EQUAL",
            "participants": [2, 3],
            "created_at": "2026-03-05T12:30:00Z"
        }
    ]

    def get(self, request):
        return Response(self.MOCK_EXPENSES, status=status.HTTP_200_OK)

    def post(self, request):
        new_expense = request.data
        new_expense["id"] = len(self.MOCK_EXPENSES) + 1
        self.MOCK_EXPENSES.append(new_expense)
        return Response(new_expense, status=status.HTTP_201_CREATED)


class BalanceListView(APIView):
    """
    Handles GET requests for balances using mock data.
    """
    MOCK_BALANCES = [
        {"id": 1, "debtor": "User1", "creditor": "User2", "amount": 500.00},
        {"id": 2, "debtor": "User3", "creditor": "User1", "amount": 300.00},
    ]

    def get(self, request):
        return Response(self.MOCK_BALANCES, status=status.HTTP_200_OK)
    
class HealthCheckView(APIView):
    """
    Health check endpoint for Docker
    """

    def get(self, request):
        return Response(
            {
                "status": "healthy",
                "service": "expense-backend"
            },
            status=status.HTTP_200_OK
        )
    