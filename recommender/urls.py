from django.urls import path
from . import views

urlpatterns = [
    path('', views.reco, name='reco'),
    path('recommend/<int:product_id>/', views.recommend_products, name='recommend_products'),
]