from django.shortcuts import render
from .serializers import SignupSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework.views import APIView

class SignupAPIView(APIView):
    
    def post(self,request):
        serializer=SignupSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                { "message": "User registered successfully"},status=201)
        
        return Response(serializer.errors,status=400)
    
class LoginAPIView(APIView):
    
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            
            user=serializer.validated_data["user"]
            
            
            refresh=RefreshToken.for_user(user)
            
            return Response(
                {
                    "message":"Login successful",
                    "access":str(refresh.access_token),
                    "refresh":str(refresh)
                },
                status=200
            )
        return Response(
            serializer.errors,
            status=400
        )
            
        
