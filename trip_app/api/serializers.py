from rest_framework import serializers

from trip_app.models import Trip, TripDetail

class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = "__all__"

class TripDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TripDetail
        fields = "__all__"
