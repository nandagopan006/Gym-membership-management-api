from rest_framework import serializers
from .models import Payment

class PaymentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Payment
        
        fields = [
            "id",
            "amount",
            "status",
            "payment_date",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]
        