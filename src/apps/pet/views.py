from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from pet.models import UserBD, OrderitemBD, OrderBD, ProductBD
from pet.serializers import UserSerializer, OrderitemSerializer, OrderSerializer, ProductSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = ProductBD.objects.all()
    serializer_class = ProductSerializer


# @api_view(['GET', 'POST', 'PUT'])
# def listView(request):
#     if request.method == 'GET':
#         object_list = OrderBD.objects.all()
#         serializer = OrderSerializer(object_list, many = True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         data = request.data
#         serializer = OrderSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer.save()
#         return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_201_CREATED,
#             )
#     if request.method == 'PUT':
#         return Response(
#                 {'status': 'Ok!'}
#             )