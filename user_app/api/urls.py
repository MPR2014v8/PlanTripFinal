from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path
from plantrip_filnal import settings
from user_app.api.views import *

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('', home_view, name='home-view'),

    path('login/', obtain_auth_token, name='login'),
    # path('register/', registration_view, name='register'),
    # path('logout/', logout_view, name='logout'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='myapp_logout'),

    path('user_all/', UserViewAV.as_view(), name='user-all'),
    path('user/<int:pk>/', UserViewDetailAV.as_view(), name='user-detail'),
    path('user/<str:username>/', UserViewDetail.as_view(), name='user-detail-view'),
    
    path('about_us/', about_us_view, name='about-us-view'),
    path('chk_group_id/<str:username>/', ChkGroupID.as_view(), name='chkgroupid-view'),
]
