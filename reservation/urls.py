from django.urls import path
from reservation.views import *

urlpatterns = [
    path("book/<id>/", book, name="book"),
    path("checkout/", checkout, name="book"),
    path("control-flow/", controlFlow, name="control_flow")
]
