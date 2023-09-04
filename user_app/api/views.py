from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from user_app import models
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics
from django.contrib.auth.models import User, Group

from user_app.api.serializers import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        if user.is_staff:
            admin_login_url = reverse('admin:login')
            return redirect(admin_login_url)
        elif user.groups.filter(name="business").exists():
            return redirect('/test/index_business/')
        else:
            messages.warning(request, 'สำหรับผู้ใช้กิจการและผู้ดูแลระบบเท่านั้น.')
            return render(request, '../templates/main/home.html', {})
    else:        
        return render(request, '../templates/main/home.html', {})
    

def about_us_view(request):
    
    return render(request, '../templates/main/about_us_page.html', {})

class ChkGroupID(generics.ListAPIView):
    
    serializer_class = UserGroupIdSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)

class UserViewAV(APIView):
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserViewDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist :
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserAccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserViewDetail(generics.ListAPIView):
    
    serializer_class = UserSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)
    

# @api_view(['POST', ])
# def logout_view(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


# @api_view(['POST', ])
# def registration_view(request):

#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)

#         data = {}

#         if serializer.is_valid():
            
#             account = serializer.save()
#             g = Group.objects.get(name="traveler")
            
#             account.groups.add(g)

#             data['response'] = "Registration Successful!"
#             data['username'] = account.username
#             data['email'] = account.email

#             token = Token.objects.get(user=account).key
#             data['token'] = token

#         else:
#             data = serializer.errors

#         return Response(data, status = status.HTTP_201_CREATED)
