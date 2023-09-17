from django.urls import path
from django.contrib.auth import views as auth_views

from test_app.views import *

app_name = 'test'

urlpatterns = [
    path('index_business/', index, name='test_index'),
    path('index_admin/', index_admin, name='test_index_admin'),
    path('login/', index_login, name='test_index_login'),
    path('logout/', logout_user, name='test_logout'),
    path('singup/', signup_business, name='test_singup_business'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    
    path('addnew', addnew, name='test_addnew'),
    path('edit/<int:pk>/', edit, name='test_edit'),
    path('update/<int:pk>/', update, name='test_update'),
    path('delete/<int:pk>', delete, name='test_delete'),
    
    path('img/<int:pk>/', image_view, name='test_image_view'),
    path('sql/', get_list_place, name='test_sql'),
    
    path('payment_add/', payment_create, name='test_payment_create'),
    path('payment/', index_payment, name='test_index_payment'),
    path('payment/<int:pk>', payment, name='test_payment'),
    path('update_payment/<int:pk>', update_payment, name='test_update_payment'),
    path('update_profile/', update_profile, name='test_update_profile'),
    
    path('get_place_distance/<int:pk>/', get_list_place_with_distance, name='test_get_place_distance'),
    path('get_place_distance2/<int:pk>/<path:lat>/<path:lng>/', get_list_place_with_distance2, name='test_get_place_distance2'),
    path('get_sortPlace_with_tripBudget/<int:pk>/', getSortPlaceWithTripBudget, name='test_get_sortPlace_with_tripBudget'),
    path('get_sortPlace_with_usePlace/', getSorPlacetWithUsePlace, name='test_get_sortPlace_with_usePlace'),
    
    path('get_sortTrip_with_useTrip/', getSorTriptWithUseTrip, name='test_get_sortTrip_with_useTrip'),
    path('get_sortTrip_with_tripBudget/<path:budget>/', getSorTriptWithtripBudget, name='test_get_sortTrip_with_tripBudget'),
    path('get_list_trip_detail_clone/<int:pk>/', getListTripDetailClone, name='test_get_list_trip_detail_clone'),
    path('get_list_rac_place/<int:pk>/', getListRacPlace, name='test_get_list_rac_place'),
    
    path('get_list_trip_user_and_pic1/<str:username>/', getListTripUserAndPic1, name='test_get_list_trip_user_and_pic1'),
    
    path(
        'add_create_trip_clone/<str:name>/<str:detail>/<str:position_start>/<str:position_end>/<path:budget>/<str:date_start>/<str:date_end>/<int:pkClone>/<str:username>/', 
        TripCloneViewAV.as_view(), 
        name='test_add_create_trip_clone'),
    
    path('add_create_trip_detail_clone/<int:pkMain>/<int:pkClone>/', addTripCloneDetail, name='test_add_create_trip_detail_clone'),
    
    path('report_business/', report, name='test_report_business'),
    path('report_business/<int:pk>/', open_report, name='test_open_report_business'),
]
