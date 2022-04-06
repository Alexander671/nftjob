# accounts/urls.py
from django.urls import path

from .views import TokensCreateView, TokensListView,TokensTotalSupplyView


urlpatterns = [
    path('create/', TokensCreateView.as_view(), name='create'),
    path('list/', TokensListView.as_view(), name='list'),
    path('total_supply/', TokensTotalSupplyView.as_view(), name='total_supply')
]  