from rest_framework import serializers
from . import models
from post.serializers import ReviewSerializer


class CrossDetailSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many = True)
    star_num = serializers.IntegerField(read_only = True)
    class Meta:
        model = models.CrossPass
        fields = '__all__'

class CrossListSerializer(serializers.ModelSerializer):
    star_num = serializers.IntegerField(read_only = True)
    class Meta:
        model = models.CrossPass
        fields = '__all__'