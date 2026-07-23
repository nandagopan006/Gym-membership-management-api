from django.shortcuts import render
from .serializers import (
    SignupSerializer,
    LoginSerializer,
    ProfileSerializer,
    MessageSerializer,
    LoginResponseSerializer,
)
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView


class SignupAPIView(APIView):

    @extend_schema(
        request=SignupSerializer,
        responses={201: MessageSerializer, 400: dict},
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message": "User registered successfully"}, status=201)

        return Response(serializer.errors, status=400)


class LoginAPIView(APIView):

    @extend_schema(
        request=LoginSerializer,
        responses={200: LoginResponseSerializer, 400: dict},
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():

            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Login successful",
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
                status=200,
            )
        return Response(serializer.errors, status=400)


class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: ProfileSerializer, 401: dict},
    )
    def get(self, request):

        serializer = ProfileSerializer(request.user)

        return Response(serializer.data, status=200)
