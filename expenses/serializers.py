from rest_framework import serializers
from expenses.models import User, Balance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ExpenseSerializer(serializers.Serializer):
    payer_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    participants = serializers.ListField(
        child=serializers.IntegerField()
    )
    split_type = serializers.CharField(default="EQUAL")


class BalanceSerializer(serializers.ModelSerializer):

    from_user = serializers.StringRelatedField()
    to_user = serializers.StringRelatedField()

    class Meta:
        model = Balance
        fields = "__all__"