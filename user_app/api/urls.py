from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path
from user_app.api.views import *

app_name = 'user'

urlpatterns = [
    path('', home_view, name='home-view'),

    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('user_all/', UserViewAV.as_view(), name='user-all'),
    path('user/<int:pk>/', UserViewDetailAV.as_view(), name='user-detail'),
    path('user/<str:username>/', UserViewDetail.as_view(), name='user-detail-view'),
    
    path('about_us/', about_us_view, name='about-us-view'),
    path('chk_group_id/<str:username>/', ChkGroupID.as_view(), name='chkgroupid-view'),
]
