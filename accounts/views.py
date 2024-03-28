from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

# Create your views here.

class SignUpView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User created successfully", 
                "user": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SigninView(APIView):
    permission_classes = [AllowAny]
    def post(self, request:Request):
        email = request.data.get("email")
        password = request.data.get("password")

        print(email)
        print(password)

        user = authenticate(email=email, password=password)
        #print(user.is_authenticated)
        if user:
            response = {
                "message": "Login successful",
                "id": user.id,
                "username": str(user),
                "token": str(user.auth_token)
            }

            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request:Request):
        data = {
            "user": str(request.user),
            "token": str(request.auth)
        }
        return Response(data=data, status=status.HTTP_200_OK)
    

