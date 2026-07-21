from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import  PaymentsSerializer

class PaymentsAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer=PaymentsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response(
                {
                    "message": "Payment created successfully"
                },status=201
            )
        return Response( serializer.errors,status=401)
    