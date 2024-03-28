from django.urls import path
from .views import RankingView, SuggestedRankingView


urlpatterns = [
    path("", RankingView.as_view(), name="ranking"),
    path("suggested", SuggestedRankingView.as_view(), name="suggested_ranking")
]