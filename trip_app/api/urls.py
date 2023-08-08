from django.urls import path

from trip_app.api.views import *

app_name = 'trip'

urlpatterns = [
    path('trip-all/', TripViewAV.as_view(), name='tripView-all'),
    path('trip/', TripSearchView.as_view(), name='tripView'),
    path('trip/<int:id>/', TripDetailViewAV.as_view(), name='tripDetailView'),
    
    path('trip-detail-all/', TripDetialPlaceViewAV.as_view(), name='tripDetailPlaceView-all'),
    path('trip-detail/', TripDetialPlaceViewAV.as_view(), name='tripDetaiPlacelView'),
    path('trip-detail/<int:id>/', TripDetailPlacelViewAV.as_view(), name='tripDetailPlaceView'),
]
