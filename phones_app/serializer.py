from django.urls import path, include
from .models import Phones
from rest_framework import serializers

# Serializers define the API representation.
class PhonesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phones
        fields = [
            'City', 
            'Date', 
            'Brand',
            'Model'
            ]

class Object1(object) :
    def __init__(self,names,values):
        self.names = names
        self.values = values
    
class TopCitySerializer(serializers.Serializer) :
    names = serializers.ListField(
        child = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    )
    values = serializers.ListField(
        child = serializers.IntegerField(min_value = 0, max_value = 100)
    )


class Object2(object) :
    def __init__(self,y,z):
        self.y = y
        self.z = z

class PhoneStorageSerializer(serializers.Serializer) :
    y = serializers.ListField(
        child = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    )
    z = serializers.ListField(
        child = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    )


class Object3(object) :
    def __init__(self,values1,values2):
        self.values1 = values1
        self.values2 = values2

class PubsValuesSerializer(serializers.Serializer) :
    values1 = serializers.ListField(
        child = serializers.DecimalField(max_digits=30,decimal_places=20)
    )

    values2 = serializers.ListField(
        child = serializers.DecimalField(max_digits=30,decimal_places=20)
    )

class Object4(object) :
    def __init__(self,storage,number):
        self.storage = storage
        self.number = number

class TopGbSerializer(serializers.Serializer) :
    storage = serializers.ListField(
        child = serializers.IntegerField(max_value=None, min_value=None)
    )

    number = serializers.ListField(
        child = serializers.DecimalField(max_digits=30,decimal_places=20)
    )
