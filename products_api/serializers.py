from rest_framework import serializers
from .models import Product
from .models import Company
from .models import UserAccount
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

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = UserAccount.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance,validated_data):
        user = UserAccount.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user
