from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here.

class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
