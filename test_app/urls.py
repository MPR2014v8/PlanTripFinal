from django.urls import path
from django.contrib.auth import views as auth_views

from test_app.views import *

app_name = 'test'

urlpatterns = [
    path('index_business/', index, name='test_index'),
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
]
