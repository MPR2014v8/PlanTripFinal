from django.urls import path

from test_app.views import *

app_name = 'test'

urlpatterns = [
    path('', index, name='test_index'),
    path('login/', index_login, name='test_index_login'),
    path('logout/', logout_user, name='test_logout'),
    path('singup/', signup_business, name='test_singup_business'),
    
    path('addnew', addnew, name='test_addnew'),
    path('edit/<int:pk>/', edit, name='test_edit'),
    path('update/<int:pk>/', update, name='test_update'),
    path('delete/<int:pk>', delete, name='test_delete'),
    
    path('img/<int:pk>/', image_view, name='test_image_view'),
    path('sql/', get_list_place, name='test_sql'),
\
]
