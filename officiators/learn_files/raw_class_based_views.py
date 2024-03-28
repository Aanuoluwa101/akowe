from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from ...rosters.serializers import OfficiatorSerializer
from ...rosters.models import Officiator

# Create your views here.

@api_view(http_method_names=["GET"])
def homepage(request:Request):
    response = {"message": "Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)

class OfficiatorListCreateView(APIView):
    serializer = OfficiatorSerializer

    def get(self, request:Request, *args, **kwargs):
        print("getting officiators")
        officiators = Officiator.objects.all()

        serializer = self.serializer(instance=officiators, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request:Request, *args, **kwargs):
        data = request.data

        serializer = OfficiatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Officiator created", "officiator": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleOfficiatorApiView(APIView):
    serializer = OfficiatorSerializer

    def get(self, request:Request, officiator_id:int):
        officiator = get_object_or_404(Officiator, pk=officiator_id)
        serializer = self.serializer(instance=officiator)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request:Request, officiator_id:int):
        officiator = get_object_or_404(Officiator, pk=officiator_id)
        serializer = self.serializer(instance=officiator, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request:Request, officiator_id:int):
        officiator = get_object_or_404(Officiator, pk=officiator_id)
        officiator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
