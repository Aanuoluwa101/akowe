from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from officiators.views import OfficiatorViewSet

router = DefaultRouter()

#what is the use of this base name
#with viewsets, we don't have to define urls in the url file of the app.
  #viewsets automatically does this for us. 
  #That is why we only have to come to the urls file of the main project to set things up

router.register("", OfficiatorViewSet, basename="officiators")   #when we use viewsets, the routes are generated for us

API_VERSION = "api/v1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{API_VERSION}/officiators/", include(router.urls)),
    path(f"{API_VERSION}/rosters/", include("rosters.urls")),
    path(f"{API_VERSION}/rankings/", include("rankings.urls")),
    path(f"{API_VERSION}/auth/", include("accounts.urls")),
    path(f"{API_VERSION}/comments/", include("comments.urls"))
]
