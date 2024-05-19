from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

class CustomLoginSerializer(LoginSerializer):
    username = None

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if self.user_exists(email, password):
                return attrs
            else:
                msg = self.error_messages['no_matching_account']
                raise serializers.ValidationError(msg)
        else:
            msg = self.error_messages['missing_fields']
            raise serializers.ValidationError(msg)

    def user_exists(self, email, password):
        self.user = self.authenticate(self.context['request'], email=email, password=password)
        return self.user is not None

    def authenticate(self, request, email=None, password=None):
        credentials = {
            'username': email, 
            'password': password
        }
        return super().authenticate(request, **credentials)