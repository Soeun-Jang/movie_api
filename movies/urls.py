from django.urls import path
from .views import MovieList, ActorList, MovieDetail,ActorDetail, review_list

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),  
    path('movies/<int:pk>/reviews', review_list),
    path('actors', ActorList.as_view()),
    path('actors/<int:pk>', ActorDetail.as_view())
]