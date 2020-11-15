from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
        read_only_fields = ['user_id', 'deleted', 'elevator_id', 'crosspass_id']

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Star
        fields = '__all__'
        read_only_fields = ["user_id", "elevator_id", "crosspass_id"]

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrier
