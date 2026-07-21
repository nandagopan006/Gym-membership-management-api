from rest_framework import serializers

from apps.users.models import User
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    class Meta :
        model=User
        fields=[
            "full_name",
            "email",
            "password",           
        ]
        extra_kwargs = {"password": {"write_only": True}
}
        
    def create(self,validated_data):
        
        return User.objects.create_user(**validated_data)
        
class LoginSerializer(serializers.Serializer):
    
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True,)
    
    def validate(self, attrs):
        
        email=attrs.get("email")
        password=attrs.get("password")

        user = authenticate(email=email,password=password)
        
        if not user :
            raise serializers.ValidationError(
                "Invalid email and password"
            )
        
        attrs["user"]=user
        
        return attrs
