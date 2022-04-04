

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from requests import get

from tokens.form import TokensForm

from .models import Tokens

# новый обьект модели Token, в который сохраняются данные из параметра запроса,
# помимо этого генерируется любая рандомная строка*,
# которая также сохраняется в созданный обьект. Объект сохраняется.
# Любая рандомная строка  - должна состоять из букв и цифр
# (т.е. без спецсимволов) и иметь длину в 20 знаков.


class TokensCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TokensForm()
        
        return render(request, 'tokens/create.html', {'form' : form})
    
    def post(self, request):
        form = TokensForm(request.POST)
        if form.is_valid():
            
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            
        return render(request, 'tokens/create.html', {'form' : form})


class TokensListView(TemplateView):
    def get(self, request, *args, **kwargs):
        tokens = Tokens.objects.all()
        
        return render(request, 'tokens/list.html', {'tokens' : tokens})
