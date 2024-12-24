from API.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from . import views

urlpatterns= [
    path('note/', views.NoteListCreate.as_view(), name='create_note'),
    path('note/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete_note'),
    path('user/register/', CreateUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include("rest_framework.urls")),
]