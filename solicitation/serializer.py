from rest_framework import serializers
from .models import Solicitation, Finances

class SolicitationSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'amount': {'read_only': True},
        }
        model = Solicitation
        fields = (
            'id',
            'product',
            'client',
            'quantity',
            'amount',
            'delivery_place'
        )

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'profit': {'write_only': True},
        }
        model = Finances
        fields = (
            "invoice_all",
            "profit"
        )

class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'invoice_all': {'write_only': True},
        }
        model = Finances
        fields = (
            "invoice_all",
            "profit"
        )