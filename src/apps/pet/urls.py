from django.contrib import admin
from django.urls import path, include
from .views import ProductAPIView

urlpatterns = [
    path('user', ProductAPIView.as_view(), name='user')
]