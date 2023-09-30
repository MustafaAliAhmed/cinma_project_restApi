"""
URL configuration for cmsCinma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movie', views.viewsets_movie)
router.register('reservation', views.viewsets_reservation)


urlpatterns = [
    path('admin/', admin.site.urls),
    # 1 - no_rest_no_model
    path('django/jsonresponsemodel/',views.no_rest_no_model),
    # 2 - no_rest_with_model
    path('django/jsonresponsefrommodel/',views.no_rest_model),
    # 3.1 - FBV Functions base views GET POST
    path('rest/fbv/',views.FBV_list),
    # 3.2 - FBV Functions base views GET PUT DELETE
    path('rest/fbv/<int:pk>',views.FBV_pk),
    # 4.1 - CBV Class base views GET POST
    path('rest/cbv/',views.CBV_list.as_view()),
    # 4.2 - CBV Class base views GET PUT DELETE
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),
    # 5.1 - mixins list
    path('rest/mixin/',views.mixins_list.as_view()),
    # 5.2 - mixins get put delete
    path('rest/mixin/<int:pk>',views.mixins_pk.as_view()), 
    # 6.1 - generics get and post
    path('rest/generic/',views.generics_list.as_view()),
    # 6.2 - generics get put delete
    path('rest/generic/<int:pk>',views.generics_pk.as_view()),
    # 7 Viewsets 
    path('rest/viewset/', include(router.urls)), 
    # 8 Find movie
    path('fbv/findmovie/', views.find_movie),
    # 9 create new reservation
    path('fbv/newreservation/', views.new_reservation),
    # 10 rest urls auth يعمل خيار اضافي لتسجيل الخروج
    path('api-auth', include('rest_framework.urls')),
    # 11 token authentication
    path('api-token-auth', obtain_auth_token),
    # 12 Post pk generics Post_pk
    # path('post/generic/',views.Post_pk.as_view()),
    path('post/generic/<int:pk>',views.Post_pk.as_view()),

]
