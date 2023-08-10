from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from trip_app.api.serializers import TripSerializer, TripDetailSerializer

from trip_app.models import Trip, TripDetail
from django.contrib.auth.models import User, Group

class TripViewAV(APIView):
    
    def get(self, request):
        users = Trip.objects.all()
        serializer = TripSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TripSearchView(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class TripDetailViewAV(APIView):
    
    serializer_class = TripSerializer

    def get(self, request, id):
        try:
            trip = Trip.objects.get(id=id)
        except Trip.DoesNotExist :
            return Response({'error': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    def put(self, request, id):
        trip = Trip.objects.get(id=id)
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        trip = Trip.objects.get(id=id)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#### Detail Place List in Trip

class TripDetialPlaceViewAV(APIView):

    def get(self, request):
        users = TripDetail.objects.all()
        serializer = TripDetailSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TripDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class TripDetailPlacelViewAV(APIView):
    
    serializer_class = TripDetailSerializer

    def get(self, request, id):
        try:
            trip = TripDetail.objects.get(id=id)
        except TripDetail.DoesNotExist :
            return Response({'error': 'TripDetail not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TripDetailSerializer(trip)
        return Response(serializer.data)

    def put(self, request, id):
        trip = TripDetail.objects.get(id=id)
        serializer = TripDetailSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        trip = TripDetail.objects.get(id=id)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TripUserViewAV(generics.ListAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Trip.objects.filter(user__username=username)
    
class TripUserIdViewAV(generics.ListAPIView):
    
    serializer_class = TripSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Trip.objects.filter(user_id=id)
    
class TripDetailIdViewAV(generics.ListAPIView):
    
    serializer_class = TripDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return TripDetail.objects.filter(trip__id=id)
    
class TripDetailPlaceAndTripIdViewAV(generics.ListAPIView):
    
    serializer_class = TripDetailSerializer

    def get_queryset(self):
        id_trip = self.kwargs['id_trip']
        id_place = self.kwargs['id_place']
        return TripDetail.objects.filter(trip__id=id_trip).filter(place__id=id_place)
    
    def delete(self):
        id_trip = self.kwargs['id_trip']
        id_place = self.kwargs['id_place']
        trip = TripDetail.objects.filter(trip__id=id_trip).filter(place__id=id_place)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class TripUserAllViewAV(generics.ListAPIView):
    
#     serializer_class = TripSerializer

#     def get_queryset(self):
#         id = self.kwargs['id']
#         return Trip.objects.filter(user_id=id)