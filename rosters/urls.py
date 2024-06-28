from django.urls import path
from .views import RosterView, RosterConvertView

urlpatterns = [
    path("", RosterView.as_view(), name="rosters"),
    path("convert", RosterConvertView.as_view(), name="file_converter")
]
