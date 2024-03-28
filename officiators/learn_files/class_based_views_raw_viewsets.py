from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from ...rosters.models import Officiator
from ...rosters.serializers import OfficiatorSerializer
from rest_framework.request import Request
from rest_framework.response import Response


class OfficiatorViewSet(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Officiator.objects.all()
        serializer = OfficiatorSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request:Request, pk=None):
        officiator = get_object_or_404(Officiator, pk=pk)
        serializer = OfficiatorSerializer(instance=officiator)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

