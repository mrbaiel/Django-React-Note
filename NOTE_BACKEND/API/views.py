from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializalizer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
from rest_framework.exceptions import ValidationError



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
     

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializalizer
    permission_classes = [IsAuthenticated]

    def  get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        try :
            serializer.save(author=self.request.user)
        except ValidationError as err:
            raise ValidationError(serializer.err) 
        

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializalizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    