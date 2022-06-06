import graphene
from graphene_django import DjangoListField, DjangoObjectType
from .models import Phones

class PhonesType(DjangoObjectType):
    class Meta:
        model = Phones
        fields = "__all__"


class Query(graphene.ObjectType):
    all_phones = graphene.List(PhonesType)
    
    def resolve_all_phones(root, info):
        return Phones.objects.all()
    
schema = graphene.Schema(query=Query)