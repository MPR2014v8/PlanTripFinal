from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from payment_app.api.serializers import PaymentSerializer

from payment_app.models import Payment

class PaymentViewAV(APIView):
    def get(self, request, id):
        pay = Payment.objects.filter(customer__id=id).filter(payment_status=False)
        serializer = PaymentSerializer(pay, many=True)
        return Response(serializer.data)
    
    def put(self, request, id):
        pay = Payment.objects.get(id=id)
        serializer = PaymentSerializer(pay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
