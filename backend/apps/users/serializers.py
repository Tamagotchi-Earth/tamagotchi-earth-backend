from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):  # noqa
    name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        cleaned_data = super(CustomRegisterSerializer, self).get_cleaned_data()
        cleaned_data['name'] = self.validated_data.get('name', '')
        return cleaned_data


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = (
            'id',
            'username',
            'email',
            'name',
            'avatar'
        )
        read_only_fields = (
            'id',
            'username',
            'email'
        )
