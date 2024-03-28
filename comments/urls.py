from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.CommentView.as_view(), name="comments")
]