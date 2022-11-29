from rest_framework.serializers import ModelSerializer
from .models import Contacts

class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contacts
        fields=['id','country_code','first_name','last_name','phone_number','contact_picture','is_favorite']

