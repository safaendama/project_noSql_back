from django.urls import path, include
from graphene_django.views import GraphQLView
from phones_app.loading import load
# from .ETL.extract import scrapping
# from .ETL.transforme import cleaning
from phones_app.schema import schema
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import *
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'topcity', TopCity)
router.register(r'storage', PhoneStorage)
router.register(r'pubs', PubsValues)
router.register(r'topgb', TopGb)
# urlpatterns = [
#     # Only a single URL to access GraphQL
#     path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
#     # path('',load)
# ]
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]