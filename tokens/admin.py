from django.contrib import admin
from .models import Tokens

class TokensAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tokens, TokensAdmin)
