from rest_framework import status, viewsets
from .models import Officiator
from .serializers import OfficiatorSerializer, UserOfficiatorsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class OfficiatorViewSet(viewsets.ModelViewSet):
    queryset = Officiator.objects.all()
    serializer_class = OfficiatorSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        #this is the function that returns all officiators
        user = request.user

        serializer = UserOfficiatorsSerializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
       

    # def create(self, request, *args, **kwargs):
    #     #this method was created so that I can guard against having duplicate officiators tied to one user


    
    #     print("executing the create method")
    #     serializer = OfficiatorSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save(secretary=self.request.user)
    #         return super().create(request, *args, **kwargs)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #after creating 

    #whenever an officiator with a new rank is added, there should be an alert to the user to update their ranking
       #remember to update ranking after you're done adding officiators
    
    #now on the ranking page. there should always be a suggested ranking and your own ranking
    #on the suggested ranking, there should be a use and edit button. 
    #our suggested ranking will contain all the ranks the user currently has. 
        #suggested ranking will be created on the addition of new officiator and saved as a file alongside ranking.json
    #when doing manual editing (adding ranks), there is a dropdown list which contains only ranks not already added
    
    def perform_create(self, serializer):
        serializer.save(secretary=self.request.user)
        return super().perform_create(serializer)