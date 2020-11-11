from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    



    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            name = validated_data['name'],
            account_type = validated_data['account_type'],

            )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "email", "name", "url","account_type","password"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "password":{"write_only":True}
        }

