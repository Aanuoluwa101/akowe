from . import views_mixins
from django.urls import path 



#we only need to set these if we are not using viewsets
urlpatterns = [
    # path("homepage/", views_keep.homepage, name="roster_homepage"),
    path("officiators/", views_mixins.OfficiatorListCreateView.as_view(), name="all_officiators"),
    path("officiators/<int:pk>", views_mixins.SingleOfficiatorApiView.as_view(), name="single_officiator"),
    path("current_user/", views_mixins.get_current_user_officiators, name="current_user")
]