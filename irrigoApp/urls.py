from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("rfid/<str:rfid>/",views.CheckRFIDExists.as_view(),name='rfid')
]