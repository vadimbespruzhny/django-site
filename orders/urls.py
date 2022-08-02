from django.urls import path
from . import views

urlpatterns = [
    path('order_create', views.order_create, name='order_create'),
]
