from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
# Products PATHS

    path('api/products', views.ProductList.as_view(), name='product_list'),

    path('api/products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),

# Company PATHS AND LOGIN

    path('api/companies', views.CompanyList.as_view(),name='company_list'),

    path('api/companies/<int:pk>', views.CompanyDetail.as_view(),name='company_detail'),

    path('api/companies/login', csrf_exempt(views.check_login), name="check_login"),

# User PATHS AND LOGIN

    path('api/users', views.UserAccountList.as_view(),name='user_list'),

    path('api/users/<int:pk>', views.UserAccountDetail.as_view(),name='user_detail'),

    path('api/users/login', csrf_exempt(views.check_user_login), name="check_user_login")

]
