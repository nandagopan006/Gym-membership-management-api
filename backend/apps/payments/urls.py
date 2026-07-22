from django.urls import path
from .views import PaymentsAPIView,PaymentStatusAPIView
urlpatterns = [
    path("",PaymentsAPIView.as_view(),name="payment"),
    path("<int:id>/",PaymentStatusAPIView.as_view(),name="payment_detial")
    
    
]