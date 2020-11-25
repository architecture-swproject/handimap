from django.shortcuts import render

import requests
import xmltodict
from django.http import HttpResponse
from . import models, serializers
from rest_framework import generics, viewsets, mixins, status
import decimal
import math
from django.db.models import Avg
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

# Create your models here.
class ElevFilter(FilterSet):
    class Meta:
        model = models.Elevator
        fields = {'sigungu':['exact']}
class ElevList(generics.ListAPIView):
    queryset = models.Elevator.objects.annotate(star_num = Avg("star__num")).all()
    serializer_class = serializers.ElevListSerializer
    filterset_class = ElevFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields=["address1", "address2", "buldNm"]
    def get(self, request, *args, **kargs):
        return self.list(self, request, *args, **kargs)

class ElevDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Elevator.objects.annotate(star_num = Avg("star__num")).all()
    serializer_class = serializers.ElevDetailSerializer



def samh(data, s):
    if data.get(s):
        return data.get(s)
    else :
        if type(s) == "int":
            return 0
        else:
            return ""

def elevdata(request):
    key = 'UoM3iK%2FWZ5ecJOUsH1jfTYWUW%2Bsro2XiSxK7AE2buutIwXlTmv18k5NGTdfUoGZnGOXZK%2Bnmf72cychHucYvdQ%3D%3D'
    sido = '서울특별시'
    gungu = ["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구","노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구", "은평구", "종로구", "중구", "중랑구"]
    addindex = 0
    for gu in gungu:
        page_url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?numOfRows=10&serviceKey='+key+'&sido='+sido+'&pageNo=1'+'&sigungu='+gu
        xml_page = xmltodict.parse(requests.get(page_url).content)
        page = math.ceil(int(xml_page['response']['body']['totalCount'])/1000)
        print(gu)
        print(page)
        for i in range(1, page+1):
            url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?numOfRows=1000&serviceKey='+key+'&sido='+sido+'&pageNo='+str(i)+'&sigungu='+gu
            data = requests.get(url).content
            xmlObject = xmltodict.parse(data)
            allData = xmlObject['response']['body']['items']['item']

            print(i)

            for data in allData:
                elevators = models.Elevator.objects.filter(elvtrMgtNo1 = data["elvtrMgtNo1"])
                elevators = elevators.filter(elvtrMgtNo2 = data["elvtrMgtNo2"])
                if len(elevators) > 0:
                    continue
                else:
                    elevator = models.Elevator()
                    elevator.sigungu = gu
                    elevator.elevatorNo = samh(data, "elevatorNo")
                    elevator.address1 = samh(data,'address1')
                    elevator.address2 = samh(data, "address2")
                    elevator.buldNm = samh(data,'buldNm')
                    elevator.buldPrpos = samh(data, "buldPropos")
                    elevator.elvtrDivNm = samh(data,'elvtrDivNm')
                    elevator.elvtrKindNm = samh(data,'elvtrKindNm')
                    elevator.elvtrMgtNo1 = samh(data, "elvtrMgtNo1")
                    elevator.elvtrMgtNo2 = samh(data, "elvtrMgtNo2")
                    elevator.elvtrModel = samh(data,'elvtrModel')
                    elevator.elvtrStts = samh(data,'elvtrStts')
                    elevator.liveLoad = samh(data,'liveLoad')
                    elevator.manufacturerName = samh(data,'manufacturerName')
                    elevator.shuttleFloorCnt = data["shuttleFloorCnt"] if data.get("shuttleFloorCnt") else 0
                    elevator.ratedCap = samh(data, "ratedCap")
                    elevator.save()
                    addindex += 1
    if addindex <= 0 :
        return HttpResponse("추가된 행이 없습니다.")
    else:
        return HttpResponse(str(addindex) + "행이 추가 되었습니다.")
