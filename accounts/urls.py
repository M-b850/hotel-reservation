from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name= "logout"),
]
