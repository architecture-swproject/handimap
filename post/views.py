from rest_framework.response import Response
from . import models
from elevator.models import Elevator
from cross_pass.models import CrossPass
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, mixins, status
from . import serializers
from rest_framework.views import APIView
from django.contrib.auth.models import User, AnonymousUser

# Create your views here.

class ReviewElevList(generics.ListCreateAPIView):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()

    def perform_create(self, serializer):
        images_data = self.request.FILES
        pk = self.kwargs.get('pk')
        elev = get_object_or_404(Elevator, pk=pk)
        review = serializer.save(user_id=self.request.user, elevator_id = elev)
        for image in images_data.getlist('image') :
            models.Photo.objects.create(review_id = review, url = image, deleted = 0)

class ReviewCrossList(generics.ListCreateAPIView):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()

    def perform_create(self, serializer):
        images_data = self.request.FILES
        pk = self.kwargs.get('pk')
        cross = get_object_or_404(CrossPass, pk=pk)
        review = serializer.save(user_id=self.request.user, crosspass_id = cross)
        for image in images_data.getlist('image') :
            models.Photo.objects.create(review_id = review, url = image, deleted = 0)

class LikeCreate(APIView):
    def get(self, request, pk):
        if type(request.user) == AnonymousUser:
            return Response("Please Login First.", status = status.HTTP_401_UNAUTHORIZED)
        else :
            review = get_object_or_404(models.Review, pk = pk)
            
            if review.like.filter(user_id = self.request.user).exists():
                review.like.filter(user_id = self.request.user).delete()
                return Response(str(pk) + "번 후기 좋아요를 취소하였습니다.")
            else:
                like_obj = models.Like()
                like_obj.review_id = get_object_or_404(models.Review, pk = pk)
                like_obj.user_id = self.request.user
                like_obj.save(user_id = self.request.user,
                                review_id = get_object_or_404(models.Review, pk = pk))
                return Response(str(pk) + "번 후기에 좋아요 하셨습니다." )

class StarElevCreate(APIView):
    def post(self, request, pk):
        
        if request.user.is_authenticated:
            return Response("Please Login First.", status = status.HTTP_401_UNAUTHORIZED)
        else :
            elev = get_object_or_404(Elevator, pk = pk)
            
            if elev.star.filter(user_id = self.request.user).exists():
                elev.star.filter(user_id = self.request.user).delete()
                return Response(str(pk) + "번 스타를 취소하였습니다.", status= status.HTTP_202_ACCEPTED)
            else:
                serializer = serializers.StarSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(elevator_id = pk, user_id = self.request.user)
                    return Response(str(pk) + "번 점수를 주셨습니다.", status = status.HTTP_201_CREATED)
class StarCrossCreate(APIView):
    def post(self, request, pk):
        user = get_object_or_404(User, pk = 1)
        if type(request.user) == AnonymousUser:
            return Response("Please Login First.", status = status.HTTP_401_UNAUTHORIZED)
        else :
            cross = get_object_or_404(CrossPass, pk = pk)
            
            if cross.star.filter(user_id = self.request.user).exists():
                cross.star.filter(user_id = self.request.user).delete()
                return Response(str(pk) + "번 스타를 취소하였습니다.", status= status.HTTP_202_ACCEPTED)
            else:
                serializer = serializers.StarSerializer(data=request.data)
                if serializer.is_valid():
                    cross = get_object_or_404(CrossPass, pk = pk)
                    serializer.save(crosspass_id = cross, user_id = user)
                    return Response(str(pk) + "번 점수를 주셨습니다.", status = status.HTTP_201_CREATED)

class Carrier(generics.ListCreateAPIView):
    queryset = models.Carrier
    serializer_class = serializers.CarrierSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

