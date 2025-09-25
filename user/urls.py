from django.urls import path

from .views import (
    UserCreateView,
    UserLoginView, ManageUserView,
)


urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="get_token"),
    path("me/", ManageUserView.as_view(), name="manage_user"),
]


app_name = "user"