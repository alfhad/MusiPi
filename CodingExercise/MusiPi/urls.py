from django.urls import path
from .views import *

urlpatterns = [
    path('song/', SongApiView.as_view()),
    path('song/<int:id>/', SongDetails.as_view()),
    path('podcast/', PodcastApiView.as_view()),
    path('podcast/<int:id>/', PodcastDetails.as_view()),
    path('audiobook/', AudioBookApiView.as_view()),
    path('audiobook/<int:id>/', AudioBookDetails.as_view()),
]
