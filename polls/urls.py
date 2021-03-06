from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import *

router =DefaultRouter()
router.register('user',UserViewset,basename="user")
router.register('auth',AuthenticateUserViewSet,basename="auth")
router.register('register',RegisterUserViewSet,basename="register")
router.register('video',videoViewset,basename="video")
router.register('article',ArticleViewset,basename="article")
router.register('newsletter',NewsletterViewset,basename="newsletter")

urlpatterns = [
    path('',include(router.urls)),
    ]