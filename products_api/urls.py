from django.urls import path
from . import views

urlpatterns = [
    path('api/products', views.ProductList.as_view(), name='product_list'),

    path('api/products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),

    path('api/companies', views.CompanyList.as_view(),name='company_list'),

    path('api/companies/<int:pk>', views.CompanyDetail.as_view(),name='company_detail'),
]
