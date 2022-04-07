from tokens import models
from rest_framework import serializers


class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tokens
        fields = "__all__"


