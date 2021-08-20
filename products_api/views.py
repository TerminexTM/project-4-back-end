# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProductSerializer
from .serializers import CompanySerializer
from .models import Product
from .models import Company


from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

def check_login(request):
    if request.method=='GET':
        return JsonResponse({})

    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        name = jsonRequest['name']
        password = jsonRequest['password']
        if Company.objects.get(name=name):
            company = Company.objects.get(name=name)
            if check_password(password, company.password):
                return JsonResponse({'id':company.id, 'name':company.name})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})
