from rest_framework import serializers
from businessplace_app.api.serializers import BusinessPlaceSerializer

from trip_app.models import Trip, TripDetail

class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = "__all__"

class TripDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TripDetail
        fields = "__all__"

# class TripDetailAllSerializer(serializers.ModelSerializer):
    
#     tripDetailAll = TripSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = TripDetail
#         fields = "__all__"