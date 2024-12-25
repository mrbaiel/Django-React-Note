from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import UserSerializer, NoteSerializalizer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
from rest_framework.exceptions import ValidationError
from .serializers import UserSerializer
from rest_framework.response import Response


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
    