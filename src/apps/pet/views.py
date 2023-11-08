from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from pet.models    import UserBD
from pet.serializers import UserSerializer


@api_view(['GET', 'POST'])
def listView(request):
    if request.method == 'GET':
        object_list = UserBD.objects.all()
        serializer = UserSerializer(object_list, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer.save()
        return Response(
                data=serializer.errors,
                status=status.HTTP_201_CREATED,
            )
        