from rest_framework import serializers
from . import models
from post.serializers import ReviewSerializer, StarSerializer

class ElevDetailSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many = True)
    star_num = serializers.IntegerField(read_only = True)
    class Meta:
        model = models.Elevator
        fields = '__all__'

class ElevListSerializer(serializers.ModelSerializer):
    star_num = serializers.IntegerField(read_only = True)
    class Meta:
        model = models.Elevator
        fields = '__all__'
