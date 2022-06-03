from django.contrib import admin
from django.urls import include, path


from django.urls import path, include
from django.views.generic import TemplateView

from nftjob.view import redirect_view
from . import api

urlpatterns = [
    path('', redirect_view),
    path('admin/', admin.site.urls),
    path('tokens/', include('tokens.urls')),
]
