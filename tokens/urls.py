# accounts/urls.py
from django.urls import path

from .views import TokensView


urlpatterns = [
    path('', TokensView.as_view(), name='tokens'),
]  