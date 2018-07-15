from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'phone']
