from django.shortcuts import render

import requests
import xmltodict
from django.http import HttpResponse
from . import models, serializers
from rest_framework import generics, viewsets, mixins, status
from django.db.models import Avg
# Create your models here.

class CrossList(generics.ListAPIView):
    queryset = models.CrossPass.objects.annotate(star_num = Avg("star__num")).all()
    serializer_class = serializers.CrossListSerializer
    def get(self, request, *args, **kargs):
        # mixins 상속으로 손쉽게 리스트 구현
        return self.list(self, request, *args, **kargs)

class CrossDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CrossPass.objects.annotate(star_num = Avg("star__num")).all()
    serializer_class = serializers.CrossDetailSerializer

def samh(data, s):
    if data.get(s):
        return data.get(s)
    else :
        if type(s) == "int":
            return 0
        else:
            return ""

def crossdata(request):
    key = 'UoM3iK%2FWZ5ecJOUsH1jfTYWUW%2Bsro2XiSxK7AE2buutIwXlTmv18k5NGTdfUoGZnGOXZK%2Bnmf72cychHucYvdQ%3D%3D'
    url = '	http://api.data.go.kr/openapi/tn_pubr_public_overpass_api?serviceKey='+key+'&pageNo=0&numOfRows=1000&type=xml'
    data = requests.get(url).content
    
    xmlObject = xmltodict.parse(data)
    addindex = 0
    allData = xmlObject['response']['body']['items']['item']
    for data in allData:
        valid = models.CrossPass.objects.filter(latitude = data["latitude"])
        valid = valid.filter(longitude = data["longitude"])
        if len(valid) > 0:
            continue
        else:
            crosspass = models.CrossPass()
            crosspass.ovrpsNm = samh(data,'ovrpsNm')
            crosspass.latitude = samh(data,'latitude')
            crosspass.longitude = samh(data,'longitude')
            crosspass.rdnmadr = samh(data,'rdnmadr')
            crosspass.handicapCvntlYn = samh(data,'handicapCvntlYn')
            crosspass.handicapCvntlType = samh(data,'handicapCvntlType')
            crosspass.handicapCvntlCo = data["handicapCvntlCo"] if data.get("handicapCvntlCo") else 0
            crosspass.save()
            addindex+=1
    if addindex <= 0:
        return HttpResponse("추가된 행이 없습니다.")
    else:
        return HttpResponse(str(addindex) + "행이 추가 되었습니다.")
