from django.urls import path

from trip_app.api.views import *

app_name = 'trip'

urlpatterns = [
    path('trip-all/', TripViewAV.as_view(), name='tripView-all'),
    
    path('trip-all/<int:pk>/', getTripId, name='getTripId'),
    
    path('trip-all-join/', get_list_trip_all, name='tripView-all'),
    path('trip-all-join/<int:pk>/', get_list_trip_all_user, name='tripView-all'),
    
    path('trip/', TripSearchView.as_view(), name='tripView'),
    
    path('trip-user/<str:username>/', TripUserViewAV.as_view(), name='tripUserView'),
    path('trip-user2/<int:pk>/', get_trip_user, name='tripUser2View'),
    
    path('trip-user-id/<int:id>/', TripUserIdViewAV.as_view(), name='tripUserIdView'),
    
    path('trip-detail-all/', TripDetialViewGetPostAV.as_view(), name='tripDetailPlaceView-all'),
    
    path('trip-detail-all-join/', get_list_trip_detail, name='tripDetailPlaceView-all'),
    path('trip-detail-all-join/<int:pk>/', get_list_trip_user_detail, name='tripDetailPlaceView-all'),
    
    path('trip-detail-all-join/<str:username>/', get_list_trip_user_detail, name='trip-detail-all-join-username'),
    
    path('trip-detail/', TripDetialViewGetPostAV.as_view(), name='trip-detail-all'),
    path('trip-detail/<int:id>/', TripDetailViewGetPutDeleteAV.as_view(), name='trip-detail-id'),
    
    path('chktrip-detail/<int:pk>/', get_count_trip_detail, name='get_count_trip_detail'),
]
