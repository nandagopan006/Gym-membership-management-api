from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class UserListAPIView(APIView):

    permission_classes = [IsAuthenticated, IsOwner]

    @extend_schema(
        responses={200: UserSerializer(many=True), 401: dict, 403: dict},
    )
    def get(self, request):

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=200)
