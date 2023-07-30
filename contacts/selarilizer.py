from rest_framework.serializers import ModelSerializer
from .models import Contacts
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'id','first_name','last_name']

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields=['id','country_code','first_name','last_name','phone_number','contact_picture','is_favorite']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = UserSerializer(instance.owner).data
        return representation