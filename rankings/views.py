from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RankingSerializer, SingleRankSerializer
from rest_framework.request import Request
from rest_framework.response import Response
import json
import os
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Rank



class RankingView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request:Request):
        # #get a user's ranking
        # ranking_file = f"data/users/{request.user.id}/rankings/ranking.json"
        # try:
        #     if not os.path.exists(ranking_file):
        #         raise FileNotFoundError
        #     with open(ranking_file, "r") as json_file:
        #         ranks = json.load(json_file)
        #     return Response(data=ranks, status=status.HTTP_200_OK)
        # except FileNotFoundError:
        #     response = {"message": "no ranking found"}
        #     return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        with open("./rankings/ranks.json", "r") as rank_file:
            ranks = json.load(rank_file)
        return Response(data=ranks, status=status.HTTP_200_OK)


    #we'll later change to aws s3 buckets to store our stuffs
    def post(self, request:Request):
        #create a ranking for a user
        data, user = request.data, request.user
        serializer = RankingSerializer(data=data)
        if serializer.is_valid():
            ranking_directory = f"data/users/{user.id}/rankings"
            if not os.path.exists(ranking_directory):
                os.makedirs(ranking_directory)
            ranking_file = os.path.join(ranking_directory, "ranking.json")
            try:
                with open(ranking_file, "w") as json_file:
                    json.dump(data, json_file, indent=2)
                response = {"message": "ranking successfully created"}
                return Response(data=response, status=status.HTTP_201_CREATED)
            except Exception as e:
                #print(f"Error creating ranking: {e}")
                raise e
                return Response(data={"message": "Error creating ranking"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request:Request):
        data, user = request.data, request.user
        serializer = RankingSerializer(data=data)

        if serializer.is_valid():
            ranking_file = f"data/users/{user.id}/rankings/ranking.json"
            try:
                if not os.path.exists(ranking_file):
                    raise FileNotFoundError
                with open(ranking_file, "w") as json_file:
                    json.dump(data, json_file, indent=2)
                return Response(data={"message": "ranking successfully updated"}, status=status.HTTP_200_OK)
            except FileNotFoundError:
                response = {"message": "no ranking found"}
                return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SuggestedRankingView(APIView):
    #if this returns an empty list, the UI should tell the user to add officiators
    def get(self, request:Request):
        User = get_user_model()
        user = User.objects.get(id=request.user.id)
        officiators = user.officiators.all()
        officiators_ranks = list(set([officiator.rank for officiator in officiators]))

        rank_data = [Rank.objects.get(name=rank) for rank in officiators_ranks if rank == "Brother" or rank == "Elder Brother"]  #we remove the  brother condition
        rank_data = [SingleRankSerializer(instance=rank).data for rank in rank_data]
        
        rank_data = sorted(rank_data, key=lambda x: x['weight'], reverse=True)
        return Response(data={"ranks": rank_data}, status=status.HTTP_200_OK)



           

