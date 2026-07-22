from django.urls import path
from .views import PaymentsAPIView,PaymentStatusAPIView,OwnerPaymentListAPIView
urlpatterns = [
    path("",PaymentsAPIView.as_view(),name="payment"),
    path("<int:id>/",PaymentStatusAPIView.as_view(),name="payment-status"),
    path("all/",OwnerPaymentListAPIView.as_view(),name="owner-payment-list"),
    
    
]