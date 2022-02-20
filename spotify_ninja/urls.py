from django.urls import path
from .views import HomeSpotifyAPIView, api

app_name = 'spotify'


urlpatterns = [
    path('', HomeSpotifyAPIView.as_view(), name='home'),
    path('api/', api.urls)
]
