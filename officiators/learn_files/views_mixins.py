from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from ...rosters.serializers import OfficiatorSerializer, UserOfficiatorsSerializer
from ...rosters.models import Officiator
#from accounts.serializers import UserOfficiatorsSerializer

# Create your views here.

@api_view(http_method_names=["GET"])
def homepage(request:Request):
    response = {"message": "Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)

class OfficiatorListCreateView(generics.GenericAPIView,
                               mixins.ListModelMixin,
                               mixins.CreateModelMixin):
    serializer_class = OfficiatorSerializer
    queryset = Officiator.objects.all()   #seems like this query set thing is a standard

    def perform_create(self, serializer):
        print("perform create called")
        user = self.request.user
        serializer.save(secretary=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        #mixins help us to skip database query and serializations etc
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    

class SingleOfficiatorApiView(generics.GenericAPIView,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin):
    serializer_class = OfficiatorSerializer
    queryset = Officiator.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def update(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(http_method_names=['GET'])
def get_current_user_officiators(request:Request):
    user = request.user

    serializer = UserOfficiatorsSerializer(instance=user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

