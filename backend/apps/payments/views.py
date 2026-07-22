from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import  PaymentsSerializer,PaymentCreateSerializer,OwnerPaymentUpdateSerializer
from .models import Payment
from django.shortcuts import get_object_or_404
from apps.users.permissions import IsOwner,IsMember

class PaymentCreateAPIView(APIView):
    permission_classes=[IsAuthenticated,IsMember]
    
    def post(self,request):
        
        serializer=PaymentCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response({
                "message": "Payment created successfully"
            },status=201)
        
        return Response(serializer.errors,status=400)

class PaymentsAPIView(APIView):
    permission_classes=[IsAuthenticated,IsMember]
    
    def get(self,request):
        
        payments=Payment.objects.filter(user=request.user)
        
        serializer=PaymentsSerializer(payments,many=True)
        
        return Response(serializer.data,status=200)
    

class PaymentStatusAPIView(APIView):
    permission_classes=[IsAuthenticated,IsMember]
    
    def get(self,request,id):
        
        payment=get_object_or_404(Payment,id=id,user=request.user)
        
        serializer=PaymentsSerializer(payment)
        
        return Response(serializer.data,status=200)

class OwnerPaymentListAPIView(APIView):
    permission_classes=[IsAuthenticated, IsOwner]
    
    def get(self,request):
        
        status_filter=request.query_params.get("status")
        
        payments=Payment.objects.all()
        
        if status_filter :
            payments=payments.filter(status=status_filter)
            
        serializer=PaymentsSerializer(payments,many=True)
        
        return Response(serializer.data,status=200)
    
class OwnerPaymentUpdateAPIView(APIView):
    permission_classes=[IsAuthenticated,IsOwner]
    
    def patch(self,request,id):
            
        payment=get_object_or_404(Payment,id=id)
        
        serializer=OwnerPaymentUpdateSerializer(payment,data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=200)
        
        return Response(serializer.errors,status=400)
            