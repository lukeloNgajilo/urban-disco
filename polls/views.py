from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Count
from .serializers import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets, status

# Create your views here.



class AuthenticateUserViewSet(viewsets.ViewSet):
    """API endpoint that allows users to login and obtain auth token."""
    # permission_classes = (AllowAny,)

    def create(self, request):
        serializer = ObtainAuthToken.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user, context={'request': request})
        data = {
            'token': token.key,
            **user_serializer.data
        }
        return Response(data)



class RegisterUserViewSet(viewsets.ViewSet):
    """API endpoint that allows users to register and obtain auth token."""
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = UserSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
         
 
        first_name = data.pop("first_name")
        middle_name = data.pop("middle_name")
        last_name = data.pop("last_name")
        gender = data.pop("gender")
        Region =data.pop("Region")
        date_of_birth=data.pop("date_of_birth")
        phone_number =data.pop("phone_number")
        Nationality=data.pop("Nationality")
        password = data.pop("password")
        username = data.pop("username")
        reg_id=Regionss.objects.get(RegionCode=Region)
       

        user = User.objects.create_user(username, password)
        
        user.first_name=first_name
        user.middle_name=middle_name
        user.last_name =last_name
        user.gender =gender
        user.Region =reg_id
        user.date_of_birth=date_of_birth
        user.phone_number =phone_number
        user.Nationality =Nationality
        user.save()

        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user, context={'request': request})
        data = {
            'token': token.key,
            **user_serializer.data
        }
        return Response(data)        

class UserViewset(QueryArgumentsMixin, EagerLoadingMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'patch', 'delete'] 

   
class videoViewset(QueryArgumentsMixin, EagerLoadingMixin, viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = videosSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']           


class NewsletterViewset(QueryArgumentsMixin, EagerLoadingMixin, viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']     

class ArticleViewset(QueryArgumentsMixin, EagerLoadingMixin, viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']  