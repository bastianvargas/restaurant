from rest_framework import serializers
from datetime import datetime

class PaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    type = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    category = serializers.CharField()
    price = serializers.IntegerField()
    name = serializers.CharField()
    quantity = serializers.IntegerField()

class ReportSerializer(serializers.Serializer):
    date_closed = serializers.DateField()
    zone = serializers.CharField()
    waiter = serializers.CharField()
    cashier = serializers.CharField()
    products = ProductSerializer(many=True)
    diners = serializers.IntegerField()
    date_opened = serializers.DateField()
    table = serializers.IntegerField()
    total = serializers.IntegerField()
    id = serializers.CharField()
    payments = PaymentSerializer(many=True)

    def validate_data_closed(self, value):
        """
        Check that the date is correct
        """
        if value != datetime:
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return value
