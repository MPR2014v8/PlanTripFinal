from django.urls import path
from businessplace_app.api.views import (
    business_home_view, business_place_view, 
    business_place_pic_view, business_place_payment_view, 
    BusinessPlaceViewAV, BusinessPlaceDetailView, BusinessPlaceSearchView,
    RatingAndCommentViewAV, RatingAndCommentSearchView, RatingAndCommentDetailView,
    RatingAndCommentFilterPlaceUser, RatingAndCommentPlace, business_login_view
)

app_name = 'business'

urlpatterns = [
    path('business_home/', business_home_view, name='businessHomeView'),
    path('business/login/', business_login_view, name='businessLoginView'),
    
    path('business-all/', BusinessPlaceViewAV.as_view(), name='businessView-all'),
    path('business/', BusinessPlaceSearchView.as_view(), name='businessView'),
    path('business/<int:id>/', BusinessPlaceDetailView.as_view(), name='businessDetailView'),
    
    path('business/place/', business_place_view, name='businessPlaceView'),
    path('business/place/pictures/', business_place_pic_view,name='businessPlacePicView'),
    path('business/place/payment/', business_place_payment_view, name='businessPlacePaymentView'),
    
    path('business/rac-all/', RatingAndCommentViewAV.as_view(), name='racView-all'),
    path('business/rac/', RatingAndCommentSearchView.as_view(), name='racView'),
    path('business/rac/<int:id>/', RatingAndCommentDetailView.as_view(), name='racDetailView'),
    path('business/rac/user=<int:id_user>,place=<int:id_place>/', RatingAndCommentFilterPlaceUser.as_view(), name='racUserPlaceView'),
    path('business/rac/place=<int:id_place>/', RatingAndCommentPlace.as_view(), name='racPlaceView'),
    
    path('business/chkin-all/', RatingAndCommentViewAV.as_view(), name='chkinView-all'),
    path('business/chkin/', RatingAndCommentSearchView.as_view(), name='chkinView'),
    path('business/chkin/<int:id>/', RatingAndCommentDetailView.as_view(), name='chkinDetailView'),
    
]
