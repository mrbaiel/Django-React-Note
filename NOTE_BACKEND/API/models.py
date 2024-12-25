from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title 
