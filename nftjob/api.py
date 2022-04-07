from rest_framework.generics import ListAPIView
from . import serializers
from tokens import models


class TokensListAPIView(ListAPIView):
    serializer_class = serializers.TokensSerializer

    def get_queryset(self):
        return models.Tokens.objects.all()

