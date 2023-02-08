from django.urls import path

from apps.user.api.views import RegisterUser

urlpatterns = [
    path('register_user', RegisterUser.as_view()),
]
