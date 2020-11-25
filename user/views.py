from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, AnonymousUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.

class UserView(APIView):

    def get(self, request):
        if type(request.user) == AnonymousUser:
            return Response("Please Login First", status=status.HTTP_401_UNAUTHORIZED)
        user = get_object_or_404(User, pk=self.request.user.id)
        serializer = serializers.UserSerializer(user)
        return Response({"user": serializer.data}, status = status.HTTP_200_OK)