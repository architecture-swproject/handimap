from django.db import models
from django.contrib.auth.models import User
from elevator.models import Elevator
from cross_pass.models import CrossPass

# Create your models here.

class Review(models.Model):
    body = models.TextField()
    user_id = models.ForeignKey(User, models.CASCADE, related_name="author")
    elevator_id = models.ForeignKey(Elevator, models.CASCADE, related_name = "review", null=True)
    crosspass_id = models.ForeignKey(CrossPass, models.CASCADE, related_name = "review", null = True)
    deleted = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    review_id = models.ForeignKey(Review, models.CASCADE, related_name = "like")
    user_id = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):
    url = models.ImageField()
    review_id = models.ForeignKey(Review, models.CASCADE)
    deleted = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Star(models.Model):
    num = models.IntegerField()
    elevator_id = models.ForeignKey(Elevator, models.CASCADE, null = True, related_name = "star")
    crosspass_id = models.ForeignKey(CrossPass, models.CASCADE, null = True, related_name= "star")
    user_id = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Carrier(models.Model):
    carrier_nm = models.CharField(max_length=100)
    type = models.CharField(max_length=20, null = True)
    weight = models.FloatField()
    width = models.FloatField(default=600)
    length = models.FloatField(default=1200)
    user_id = models.OneToOneField(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)