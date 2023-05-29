from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions



# ------ VIEWS ------

def index(request):
    return render(request, 'index.html', {})


class UserViewSet(ModelViewSet):        # ModelViewSet class permits retrieving a list of users, creating a new user, updating an existing user, and deleting a user
    queryset = User.objects.all()       # User is the default user model provided by Django's built-in authentication system
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer


