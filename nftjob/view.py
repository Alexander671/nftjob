
from django.http import HttpResponse
from django.shortcuts import redirect, render
def redirect_view(request):
    return render(request, 'home.html', {})
