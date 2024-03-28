from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ...rosters.serializers import OfficiatorSerializer
from ...rosters.models import Officiator

# Create your views here.

@api_view(http_method_names=["GET"])
def homepage(request:Request):
    response = {"message": "Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET", "POST"])
def officiators(request:Request):
    if request.method == 'POST':
        data = request.data

        serializer = OfficiatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Officiator created", "officiator": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    officiators = Officiator.objects.all()
    serializer = OfficiatorSerializer(instance=officiators, many=True)

    response = {"user_id": 123, "officiators": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def officiator(request:Request, officiator_id:int):
    officiator = get_object_or_404(Officiator, pk=officiator_id)

    serializer = OfficiatorSerializer(instance=officiator)

    # we don't need this because we are using get_object_or_404
    # if officiator:
    #     return Response(data=officiator, status=status.HTTP_200_OK)
    # return Response(data={"error": "officiator not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
