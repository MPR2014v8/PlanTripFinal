from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from businessplace_app.api.serializers import BusinessPlaceSerializer, RatingAndCommentSerializer
from rest_framework.response import Response
from businessplace_app.models import BusinessPlace, RatingAndComment
from rest_framework import filters
from rest_framework import generics
from rest_framework import status


def business_login_view(request):
    return render(request, '../templates/business_login_page.html', {})

def business_home_view(request):
    return render(request, '../templates/business_home_page.html', {})

def business_place_view(request):
    return render(request, '../templates/business_place_manage_page.html', {})

def business_place_pic_view(request):
    return render(request, '../templates/business_place_pic_manage.html', {})

def business_place_payment_view(request):
    return render(request, '../templates/business_place_payment_manage.html', {})

class BusinessPlaceCreateViewAV(APIView):
    
    def get(self, request):
        place = BusinessPlace.objects.all()
        serializer = BusinessPlaceSerializer(place, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BusinessPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessPlaceUserViewAV(generics.ListAPIView):
    serializer_class = BusinessPlaceSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return BusinessPlace.objects.filter(place_user__username=username)

class BusinessPlaceViewAV(APIView):
    
    def get(self, request):
        users = BusinessPlace.objects.all()
        serializer = BusinessPlaceSerializer(users, many=True)
        return Response(serializer.data)
    
class BusinessPlaceSearchView(generics.ListAPIView):
    queryset = BusinessPlace.objects.all()
    serializer_class = BusinessPlaceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class BusinessPlaceDetailView(generics.ListAPIView):
    serializer_class = BusinessPlaceSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return BusinessPlace.objects.filter(id=id)
    
class RatingAndCommentViewAV(APIView):
    
    def get(self, request):
        users = RatingAndComment.objects.all()
        serializer = RatingAndCommentSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RatingAndCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RatingAndCommentSearchView(generics.ListAPIView):
    queryset = RatingAndComment.objects.all()
    serializer_class = RatingAndCommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['place__name']
    
class RatingAndCommentDetailView(APIView):
    serializer_class = RatingAndCommentSerializer

    def get(self, request, id):
        try:
            rac = RatingAndComment.objects.get(id=id)
        except RatingAndComment.DoesNotExist :
            return Response({'error': 'RatingAndComment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RatingAndCommentSerializer(rac)
        return Response(serializer.data)

    def put(self, request, id):
        rac = RatingAndComment.objects.get(id=id)
        serializer = RatingAndCommentSerializer(rac, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rac = RatingAndComment.objects.get(id=id)
        rac.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RatingAndCommentFilterPlaceUser(generics.ListAPIView):
    serializer_class = RatingAndCommentSerializer

    def get_queryset(self):
        id_user = self.kwargs['id_user']
        id_place = self.kwargs['id_place']
        return RatingAndComment.objects.filter(user__id=id_user).filter(place__id=id_place)
    
class RatingAndCommentPlace(generics.ListAPIView):
    serializer_class = RatingAndCommentSerializer

    def get_queryset(self):
        id_place = self.kwargs['id_place']
        return RatingAndComment.objects.filter(place__id=id_place)





# class checkInLocationPlaceViewAV(APIView):
    
#     def get(self, request):
#         users = RatingAndComment.objects.all()
#         serializer = RatingAndCommentSerializer(users, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = RatingAndCommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class checkInLocationPlaceSearchView(generics.ListAPIView):
#     queryset = RatingAndComment.objects.all()
#     serializer_class = RatingAndCommentSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['place__name']
    
# class checkInLocationPlaceDetailView(APIView):
#     serializer_class = RatingAndCommentSerializer

#     def get(self, request, id):
#         try:
#             rac = RatingAndComment.objects.get(id=id)
#         except RatingAndComment.DoesNotExist :
#             return Response({'error': 'RatingAndComment not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = RatingAndCommentSerializer(rac)
#         return Response(serializer.data)

#     def put(self, request, id):
#         rac = RatingAndComment.objects.get(id=id)
#         serializer = RatingAndCommentSerializer(rac, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         rac = RatingAndComment.objects.get(id=id)
#         rac.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)