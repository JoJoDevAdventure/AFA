import numpy as np
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


class LatestProductsList(APIView):
    def get(self, request, format=None) :
        products = np.random.choice(Product.objects.all(), size=4, replace=False)
        serializer = ProductSerializer (products, many=True)
        return Response (serializer.data)
    
class LatestCollectionsList(APIView):
    def get(self, request, format=None) :
        collections = np.random.choice(Collection.objects.all(), size=3, replace=False)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get_object (self, collection_slug, product_slug) :
        try:
            return Product.objects.filter(collection__slug=collection_slug).get(slug=product_slug)
        except Product. DoesNotExist:
            raise Http404
        
    def get (self, request, collection_slug, product_slug, format=None):
        product = self.get_object(collection_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
class CollectionsList(APIView):
    def get(self, request, format=None) :
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response (serializer.data)


class CollectionDetails(APIView):
    def get_object (self, collection_slug) :
        try:
            return Collection.objects.get(slug=collection_slug)
        except Product. DoesNotExist:
            raise Http404
        
    def get (self, request, collection_slug, format=None):
        collection = self.get_object(collection_slug)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

class CollectionProducts(APIView):
    def get_object (self, collection_slug) :
        try:
            return Product.objects.filter(collection__slug=collection_slug).all()
        except Product.DoesNotExist:
            raise Http404
        
    def get (self, request, collection_slug, format=None):
        products = self.get_object(collection_slug)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
