from django.urls import path
from businessplace_app.api.views import *
from payment_app.api.views import PaymentViewAV

app_name = 'payment'

urlpatterns = [
    path('payment/<int:id>/', PaymentViewAV.as_view(), name='paymentView'),
]
