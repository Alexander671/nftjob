# accounts/urls.py
from django.urls import path

from .views import TokensCreateView, TokensListView


urlpatterns = [
    path('create/', TokensCreateView.as_view(), name='create'),
    path('list/', TokensListView.as_view(), name='list'),
]  