from rest_framework import serializers
from .models import Payment

class PaymentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Payment
        
        fields = [
            "id",
            "amount",
            "status",
            "created_at",
        ]

class PaymentCreateSerializer(serializers.ModelSerializer):
    
    class Meta :
        model=Payment
        fields=["amount"]

class OwnerPaymentUpdateSerializer(serializers.ModelSerializer):
    class Meta :
        model=Payment
        fields=["status"]