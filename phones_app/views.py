from unittest import result
from django.shortcuts import render
from .models import Phones
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import *
from .search import search
import pandas as pd
import numpy as np

# Create your views here.
class PhonesViewSet(viewsets.ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer



def PhonesDataFrame() :
    result = search()

    df = pd.DataFrame([{
        'id' : r.meta.id,
        **r.to_dict()
    }
    for r in result
    ])
    return df

class TopCity(viewsets.ViewSet) :
    
    df= PhonesDataFrame()
    city_name=df.City.value_counts().index
    city_val=df.City.value_counts().values
    # df.set_index(['date','id'],inplace = True)

    obj = Object1(city_name,city_val)

    queryset = Phones.objects.all()
    def list(self,request)  :
        serializer = TopCitySerializer(self.obj)

        return Response(serializer.data)

class PhoneStorage(viewsets.ViewSet) :

    df= PhonesDataFrame()
    y = df.groupby(by="Storage")["Price"].mean()
    y = list(y)
    z = df.groupby(by="Brand")["Price"].mean()
    z = list(z)
    obj = Object2(y,z)

    queryset = Phones.objects.all()
    def list(self,request)  :
        serializer = PhoneStorageSerializer(self.obj)

        return Response(serializer.data)

        
class PubsValues(viewsets.ViewSet) :

    df= PhonesDataFrame()

    e=df.groupby(by="Stat")["Price"].mean()

    Stat_val=df.Stat.value_counts().values
    
    obj = Object3(list(e),list(Stat_val))
    queryset = Phones.objects.all()
    def list(self,request)  :
        serializer = PubsValuesSerializer(self.obj)

        return Response(serializer.data)

class TopGb(viewsets.ViewSet) :
    
    df= PhonesDataFrame()
    count = df.groupby(['Brand','Storage']).size().reset_index().rename(columns={0:'number Count'})
    storage = count['Storage']
    number = count['number Count']
    obj = Object4(list(storage),list(number))
    queryset = Phones.objects.all()
    def list(self,request)  :
        serializer = TopGbSerializer(self.obj)

        return Response(serializer.data)
    
def test() :
    df= PhonesDataFrame()
    count = df.groupby(['Brand','Storage']).size().reset_index().rename(columns={0:'number Count'})
    return count