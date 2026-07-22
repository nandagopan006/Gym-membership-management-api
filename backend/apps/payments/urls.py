from django.urls import path
from .views import PaymentsAPIView,PaymentStatusAPIView,OwnerPaymentListAPIView,OwnerPaymentUpdateAPIView,PaymentCreateAPIView
urlpatterns = [
    path("",PaymentsAPIView.as_view(),name="payment"),
    path("create/",PaymentCreateAPIView.as_view(),name="payment-create  "),
    path("<int:id>/",PaymentStatusAPIView.as_view(),name="payment-status"),
    path("all/",OwnerPaymentListAPIView.as_view(),name="owner-payment-list"),
    path("<int:id>/update/",OwnerPaymentUpdateAPIView.as_view(),name="owner-payment-update"),
    
    
    
]