from rest_framework import serializers


class ExpenseSerializer(serializers.Serializer):

    payer_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    participants = serializers.ListField(
        child=serializers.IntegerField()
    )
    split_type = serializers.CharField()
    metadata = serializers.ListField(required=False)