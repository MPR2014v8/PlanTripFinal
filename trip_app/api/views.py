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

import json
from django.db import connection
from django.http import HttpResponse

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

def get_list_trip_detail(request):

    data_list = []
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                td.id as id_trip_detail,
                td.created_datetime as created_datetime_trip_detail,
                td.change_datetime as change_datetime_trip_detail,
                place_id,
                p.name as place_name,
                lat,
                lng,
                minPrice,
                maxPrice,
                trip_id,
                t.name as trip_name,
                t.budget as trip_budget,
                user_id,
                username
            FROM PLANTRIPDB.TripDetail as td
            inner join PLANTRIPDB.Trip as t on td.trip_id = t.id
            inner join PLANTRIPDB.BusinessPlace as p on td.place_id = p.id
            inner join PLANTRIPDB.auth_user as u on u.id = user_id;       
        """)
        data_read = cursor.fetchall()
        print(data_read[0])

    for row in data_read:
        data_list.append({
            "id_trip_detail": str(row[0]),
            "created_datetime_trip_detail": str(row[1]),
            "change_datetime_trip_detail": str(row[2]),
            "place_id": str(row[3]),
            "place_name": str(row[4]),
            "lat": str(row[5]),
            "lng": str(row[6]),
            "minPrice": str(row[7]),
            "maxPrice": str(row[8]),
            "trip_id": str(row[9]),
            "trip_name": str(row[10]),
            "trip_budget": str(row[11]),
            "user_id": str(row[12]),
            "username": str(row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response

def get_trip_user(request, pk):

    data_list = []
    with connection.cursor() as cursor:
        sql = f"""
            SELECT * FROM PLANTRIPDB.Trip as t
            WHERE t.id = {pk};
        """
        cursor.execute(sql)
        data_read = cursor.fetchall()
        print(data_read[0])

    for row in data_read:
        data_list.append({
            "id": str(row[0]),
            "name": str(row[1]),
            "detail": str(row[2]),
            "position_start": str(row[3]),
            "position_end": str(row[4]),
            "budget": str(row[5]),
            "permission": str(row[6]),
            "created_datetime": str(row[7]),
            "change_datetime": str(row[8]),
            "user_id": str(row[-1]),
        })

    json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
    response = HttpResponse(
        json_data, content_type='application/json; charset=utf-8')

    return response

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
    
# class TripUserAllViewAV(generics.ListAPIView):
    
#     serializer_class = TripSerializer

#     def get_queryset(self):
#         id = self.kwargs['id']
#         return Trip.objects.filter(user_id=id)