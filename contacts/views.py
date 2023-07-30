from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contacts
from .selarilizer import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
import os
from django.conf import settings
import json
from rest_framework import status
from django.views.static import serve

def ServerJavascript(request):
    base_path = os.path.join(settings.BASE_DIR,'api_scripts')
    js_path = os.path.join(base_path, 'states_pin.js')
    print(base_path,js_path)
    return serve(request,path=js_path)

class states_pin(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        states_data = []
        file_path = os.path.join(settings.BASE_DIR, 'data_set/states_dist.json')
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for values in data:
                states_data.append(values['state'])
        return Response(list(states_data),status=status.HTTP_200_OK)

    def post(self,request):
        search_str = request.data['state']
        if search_str == 'Choose...':
            data_a = {'not_state'}
            return Response(list(data_a), status=status.HTTP_200_OK)
        file_path = os.path.join(settings.BASE_DIR, 'data_set/states_dist.json')
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for v in data:
                x = v['state']
                if x == search_str:
                    data_dist = v['districts']
        data_a = data_dist
        return Response(list(data_a),status=status.HTTP_200_OK)

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

def video_p2p(request):
    return render(request, 'contacts/video_p2p/base.html')
def video_p2p_room(request):
    return render(request, 'contacts/video_p2p/room.html')

@api_view(['POST'])
def ReverseString(request):
    input = request.data.get('input')
    output = input[::-1]
    return Response({'output': output})