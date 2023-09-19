from django.urls import path

from trip_app.api.views import *

app_name = 'trip'

urlpatterns = [
    path('trip-all/', TripViewAV.as_view(), name='tripView-all'),
    
    path('trip-all/<int:pk>/', getTripId, name='getTripId'),
    
    path('trip-all-join/', get_list_trip_all, name='tripView-all'),
    path('trip-all-join/<int:pk>/', get_list_trip_all_user, name='tripView-all'),
    
    path('trip-detail-id-all/<int:id>/', TripDetailIdViewAV.as_view(), name='tripDetailIdView-all'),
    path('trip-detail-id/<int:id_trip>/<int:id_place>/', TripDetailPlaceAndTripIdViewAV.as_view(), name='tripPlaceAndTripIdView-all'),
    
    path('trip/', TripSearchView.as_view(), name='tripView'),
    path('trip/<int:id>/', TripDetailViewAV.as_view(), name='tripDetailView'),
    
    path('trip-user/<str:username>/', TripUserViewAV.as_view(), name='tripUserView'),
    path('trip-user2/<int:pk>/', get_trip_user, name='tripUser2View'),
    
    path('trip-user-id/<int:id>/', TripUserIdViewAV.as_view(), name='tripUserIdView'),
    
    path('trip-detail-all/', TripDetialPlaceViewAV.as_view(), name='tripDetailPlaceView-all'),
    
    path('trip-detail-all-join/', get_list_trip_detail, name='tripDetailPlaceView-all'),
    path('trip-detail-all-join/<int:pk>/', get_list_trip_user_detail, name='tripDetailPlaceView-all'),
    
    path('trip-detail/', TripDetialPlaceViewAV.as_view(), name='tripDetaiPlacelView'),
    path('trip-detail-id/<int:pk>/', getTripDetailId, name='getTripDetailId'),
    path('trip-detail-put-delete/<int:id>/', TripDetailPlacelViewAV.as_view(), name='tripDetailPlaceView'),
    
    path('chktrip-detail/<int:pk>/', get_count_trip_detail, name='get_count_trip_detail'),
     
    path('get_list_trip_user_detail_with_username/<str:username>/', get_list_trip_user_detail_with_username, name='get_list_trip_user_detail_with_username'),

]
