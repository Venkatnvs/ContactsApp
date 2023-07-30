from django.urls import path
from .views import ContactList, ContactDetail, states_pin,ServerJavascript

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactDetail.as_view()),
    path('states_pins/', states_pin.as_view(), name='home'),
    path('statejs/v1/js', ServerJavascript, name='hometestserver')
]