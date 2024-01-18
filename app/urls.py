from django.urls import path
from app import views

urlpatterns = [
    path('api_products/', views.api_products, name='apiProducts' ),
    path('getProductDetails/<int:product_id>/', views.getProductDetails, name='getProductDetails' ),
]
