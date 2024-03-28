from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=50)
    comment = serializers.CharField(max_length=1000)

    class Meta:
        model = Comment
        fields = '__all__'
