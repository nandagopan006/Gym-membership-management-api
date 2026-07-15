from rest_framework import serializers

from apps.users.models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta :
        model=User
        fields=[
            "full_name",
            "email",
            "password",           
        ]
        extra_kwagrs={"password":{"write_only":True}}
        
        def create(self,validated_data):
            
            return User.objects.user_create(**validated_data)
        
    
    