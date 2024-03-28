from django.urls import path
from . import views

urlpatterns = [
    path('comments/', view=views.CommentView.as_view(), name="comments")
]