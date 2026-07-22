from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import  PaymentsSerializer
from .models import Payment
from django.shortcuts import get_object_or_404
from apps.users.permissions import IsOwner

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
    
    def get(self,request):
        
        payments=Payment.objects.filter(user=request.user)
        
        serializer=PaymentsSerializer(payments,many=True)
        
        return Response(serializer.data,status=200)
    
class PaymentStatusAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,id):
        
        payment=get_object_or_404(Payment,id=id,user=request.user)
        
        serializer=PaymentsSerializer(payment)
        
        return Response(serializer.data,status=200)

class OwnerPaymentListAPIView(APIView):
    permission_classes=[IsAuthenticated,IsOwner]
    
    def get(self,request):
        
        payments=Payment.objects.all()
        serializer=PaymentsSerializer(payments,many=True)
        
        return Response(serializer.data,status=200)
    
class OwnerPaymentUpdateAPIView(APIView):
    permission_classes=[IsAuthenticated,IsOwner]
    
    def patch(self,request,id):
        
        payment=get_object_or_404(Payment,id=id)
        serializer=PaymentsSerializer(payment,data=request.data,partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data,status=200)
        
        return Response(serializer.errors,status=400) 