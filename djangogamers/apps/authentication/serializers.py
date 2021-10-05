import enum

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from djangogamers.apps.authentication.models import User, Gamer, Developer, Publisher, StaffMember


class RegistrationSerializer(serializers.ModelSerializer):
    class Roles(enum.Enum):
        GAMER = "GAMER", "Gamer"
        DEVELOPER = "DEVELOPER", "Developer"
        PUBLISHER = "PUBLISHER", "Publisher"
        STAFFMEMBER = "STAFFMEMBER", "StaffMember"

    password = serializers.CharField(
        min_length=6, max_length=100, write_only=True
    )
    roles = [role.value for role in Roles]
    type = serializers.ChoiceField(choices=roles, required=True)
    first_name = serializers.CharField(max_length=100, required=True)
    email = serializers.CharField(max_length=100, required=True,
                                  validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password', 'type', ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        type = self.validated_data['type']
        if type == 'GAMER':
            user = Gamer.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        elif type == 'DEVELOPER':
            user = Developer.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        elif type == 'PUBLISHER':
            user = Publisher.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                type=type,
                is_active=True
            )
        else:
            user = StaffMember.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['role'] = user.type
        token['username'] = user.username

        return token
