# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
