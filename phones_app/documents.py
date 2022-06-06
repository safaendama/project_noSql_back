from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Phones

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'phones'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Phones
         fields = [
             'Price',
             'City',
             'Date',
             'Brand',
             'Model',
             'Storage',
             'Stat'

         ]