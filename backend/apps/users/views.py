from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListAPIView(APIView):
    
    permission_classes=[IsAuthenticated,IsOwner]

    def get(self,request):
        
        users=User.objects.all()
        
        serializer=UserSerializer(users,many=True)
        
        return Response(serializer.data,status=200)