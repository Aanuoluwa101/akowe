from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        print("running custom validation")
        #this method is called for custom validation after the validations defined above (email, username etc)
        #has passed. the validated data is put in attrs
        user_exists = User.objects.filter(email=attrs['email']).exists()

        if user_exists:
            raise ValidationError("Email already taken")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        print("running custom user creation")
        #this method is called when we call serializer.save(). it creates the object
        password = validated_data.pop("password")

        user = super().create(validated_data)  #creating doesn' mean we are saving it
        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user
    

