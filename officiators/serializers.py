from rest_framework import serializers
from .models import Officiator
from django.contrib.auth import get_user_model


class OfficiatorSerializer(serializers.ModelSerializer):
    # secretary = serializers.CharField(allow_blank=True)
    class Meta:
        model = Officiator
        fields= '__all__'
        extra_kwargs = {
            "secretary": {"required": False, "allow_null": True, "write_only": True}  #when do you use extra_kwargs
        }

class UserOfficiatorsSerializer(serializers.ModelSerializer):
    #a serializer that returns info about a user and the officiators attached to that user
    #try changing the name of this officiators to officiator
    #also try removing a field and see if it will be serialized
    officiators = OfficiatorSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ["id", "officiators"]   #we needed to add the officiators field to the list of fields

