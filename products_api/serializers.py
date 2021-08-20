from rest_framework import serializers
from .models import Product
from .models import Company

from django.contrib.auth.hashers import make_password, check_password

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description', 'price', 'category', 'business_name', 'business_id', )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'password',)


    def create(self, validated_data):
        company = Company.objects.create(
        name=validated_data['name'],
        password = make_password(validated_data['password'])
        )
        company.save()
        return company

    def update(self,instance,validated_data):
        company = Company.objects.get(name=validated_data['name'])
        company.password = make_password(validated_data['password'])
        company.save()
        return company
