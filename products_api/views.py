# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProductSerializer
from .serializers import CompanySerializer
from .serializers import UserAccountSerializer
from .models import Product
from .models import Company
from .models import UserAccount


from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Product Views
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

# Company Views
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

# User views
class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

#Company Auth function
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
# User Auth function
def check_user_login(request):
    if request.method=='GET':
        return JsonResponse({})

    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']
        if UserAccount.objects.get(username=username):
            user = UserAccount.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id':user.id, 'username':user.username})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})
