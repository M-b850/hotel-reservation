from django.urls import path
from hotels.views import *

urlpatterns = [path("", Index.as_view())]
