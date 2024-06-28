from django.conf import settings
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import FileUploadSerializer
from .serializers import RosterDataSerializer, RosterSerializer
from .engine.roster_maker import RosterMaker
from .engine.utils import get_user_rosters
import convertapi
import json
import os
from dotenv import load_dotenv



class RosterView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request:Request):
        #for now, this should return all rosters associated with the user, with frontend filtering
        #later when rosters increase, we'll do pagination.
        #people should not be able to change their username for now

        rosters = get_user_rosters(request.user.id)
        if rosters is not None:
            return Response(data=rosters, status=status.HTTP_200_OK)
        return Response(data={"message": "Error fetching rosters"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request:Request):
        #in the frontend, make sure they can't enforce two people on thesame day and activity
        data = request.data
        print(json.dumps(data))
        serializer = RosterDataSerializer(data=request.data)
        if serializer.is_valid():
            #data["username"] = request.user.username


            # data["user_id"] = request.user.id
            #for TESTING
            # data["username"] = data["temp_user"]
            # data["email"] 

            #return Response(data=data, status=status.HTTP_201_CREATED)  #for now
            print("MAKING ROSTER")
            #print(data)
            roster_maker = RosterMaker()
            roster = roster_maker.make_roster(data)
            if roster: 
                 return Response(data=roster, status=status.HTTP_201_CREATED)
            return Response(data={"message": "Error creating roster"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request:Request):
        #for now, we won't be deleting any roster
        pass

    def put(self, request:Request):
        roster = request.data
        serializer = RosterSerializer(data=roster)

        if serializer.is_valid():
            username, month, year = request.user.username, roster["month"], roster["year"]
            roster_file = f"data/users/{username}/rosters/{year}/{month}.json"
            try:
                if not os.path.exists(roster_file):
                    raise FileNotFoundError
                with open(roster_file, "w") as json_file:
                    json.dump(roster, json_file, indent=2)
                return Response(data=roster, status=status.HTTP_200_OK)
            except FileNotFoundError:
                response = {"message": f"{month} {year} roster not found for {username}"}
                return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


load_dotenv()        
convertapi.api_secret = os.getenv('CONVERTAPI_SECRET_KEY')

from django.http import HttpResponse


class RosterConvertView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        roster_html = request.FILES['roster']
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            roster_html = request.FILES['roster']
            input_file_path = os.path.join(roster_html.name)

            # Save uploaded file
            with open(input_file_path, 'wb+') as destination:
                for chunk in roster_html.chunks():
                    destination.write(chunk)

            try:
                # Get the base name without the extension
                base_name = os.path.splitext(roster_html.name)[0]
                
                # Convert file
                result = convertapi.convert('docx', {
                    'File': input_file_path
                }, from_format='html')

                # Save converted file
                output_file_name = f'{base_name}.docx'
                result.save_files(output_file_name)
                
                #Return converted file
                with open(output_file_name, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                    response['Content-Disposition'] = f'attachment; filename="{output_file_name}"'
                    
                    return response

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
