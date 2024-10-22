from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.TourList.as_view()),
    path('tours/<int:pk>/', views.TourDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('bands/', views.BandList.as_view()),
    path('bands/<int:pk>/', views.BandDetail.as_view()),
    path('genres/', views.GenreList.as_view())
]