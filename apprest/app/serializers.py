from rest_framework import serializers
from .models import company, session, user, role
from rest_framework.settings import api_settings

class SerializerWithToken(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)
        token = serializers.SerializerMethodField()
        def get_token(self, object):
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(object)
                token = jwt_encode_handler(payload)
                return token

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = user
                fields = ('id', 'name', 'last_name', 'email',
                        'active', 'date_created', 'date_modified', 
                        'user_created', 'user_modified', 'id_company', 
                        'password', 'id_role', 'phone', 'phone_mobile', 
                        'code_phone_country')
        read_only_fields = ('date_created', )

class RoleSerializer(serializers.ModelSerializer):
        class Meta:
                model = role
                fields = ('id', 'name', 'description', 'active')

class CompanySerializer(serializers.ModelSerializer):
        class Meta:
                model = company
                fields = ('id', 'name', 'address', 'contact_phone',
                        'active', 'date_created', 'date_modified', 
                        'user_created', 'user_modified')
        read_only_fields = ('date_created', )

class SessionSerializer(serializers.ModelSerializer):
        class Meta:
                model = session
                fields = ('id', 'session_on', 'session_out', 
                        'token_bearer', 'active', 'iduser', 'idapp')
        read_only_fields = ('session_on', )
        