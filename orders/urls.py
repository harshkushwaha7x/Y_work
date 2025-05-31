from django.urls import path
from .views import OrderListCreateAPIView, GoogleLogin

urlpatterns = [
    path('', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
] 