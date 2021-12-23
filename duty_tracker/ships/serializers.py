from rest_framework import serializers
from .models import Ship, ShipClass, Feature, TransferRequest
from django.contrib.auth import get_user_model
User = get_user_model()


class ShipClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipClass
        fields = ['id', 'name', 'complement']

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ['id', 'name', 'complement']

class TransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = ['id', 'name', 'complement']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'rank', 'ship']