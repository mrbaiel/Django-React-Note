from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializalizer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
     
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializalizer
    permission_classes = ["IsAuthenticated"]