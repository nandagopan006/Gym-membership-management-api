from django.urls import path
from .views import PaymentsAPIView
urlpatterns = [
    path("",PaymentsAPIView.as_view(),name="payment"),
    
    
]