from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contacts
from .selarilizer import ContactSerializer
from rest_framework import permissions

class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Contacts.objects.filter(owner=self.request.user)

class ContactDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field="id"
    
    def get_queryset(self):
        return Contacts.objects.filter(owner=self.request.user)