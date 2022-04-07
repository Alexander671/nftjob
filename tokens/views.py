

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import get
from nftjob import settings

from tokens.form import TokensForm
from .models import Tokens


from web3 import Web3
from web3.middleware import geth_poa_middleware


import environ


# новый обьект модели Token, в который сохраняются данные из параметра запроса,
# помимо этого генерируется любая рандомная строка*,
# которая также сохраняется в созданный обьект. Объект сохраняется.
# Любая рандомная строка  - должна состоять из букв и цифр
# (т.е. без спецсимволов) и иметь длину в 20 знаков.

from random import choice
from string import ascii_letters

# /tokens/create 
# Метод запроса: POST
# Это API должно создавать новый уникальный токен в блокчейне 
# и записывать параметры запроса в БД.
class TokensCreateView(TemplateView):
    template_name = 'tokens/create.html'
    
    def get(self, request, *args, **kwargs):
        form = TokensForm()
        return render(request, 'tokens/create.html', {'form' : form})


    def post(self, request):
        form = TokensForm(request.POST)
        
        # инициализация смарт контракта
        contract_instance, block, gas_price, w3 = connect_smart_contract()
        
        # случайная строка
        # реализовать проверку на уникальность?
        unique_hash = ''.join(choice(ascii_letters + ''.join(map(str, range(0,10)))) for i in range(20))
        
        # файл с приватным ключом 
        # в формате мнемонической фразы
        encrypted_key = settings.PRIVATE_KEY

        # The use of the Mnemonic features of Account is disabled 
        # by default until its API stabilizes.
        # To use these features, please enable them by running
        w3.eth.account.enable_unaudited_hdwallet_features()
        
        # create private_key
        account = w3.eth.account.from_mnemonic(encrypted_key)
        
        # nonce
        nonce = w3.eth.get_transaction_count(settings.ME)  
        
        # mint
        unicorn_txn = contract_instance.functions.mint(
            request.POST['owner'],
            unique_hash,
            request.POST['media_url']).buildTransaction({
        'from'  : settings.ME,
        'nonce' : nonce})
        

        # create signature
        signed = w3.eth.account.sign_transaction(unicorn_txn, account.privateKey)
        
        # выполнение транзакции и получение ответа
        hash_transaction = w3.eth.send_raw_transaction(signed.rawTransaction)  


        if form.is_valid():
            
            # save params
            req = form.save(commit=False)
            req.unique_hash = unique_hash
            req.tx_hash = hash_transaction
            req.save()
            
        return render(request, 'tokens/create.html', {'form' : form})


# /tokens/list
# Метод запроса: GET
# Это API  должно выдавать список всех обьектов модели Token
class TokensListView(TemplateView):
    def get(self, request, *args, **kwargs):
        tokens = Tokens.objects.all()
        
        return render(request, 'tokens/list.html', {'tokens' : tokens})

# /tokens/total_supply
# Метод запроса: GET
# Это API должно обращаться к контракту в блокчейне и выдавать
# в ответе информацию о текущем Total supply токена - общем числе 
# находящихся токенов в сети. Форма ответа - произвольная, в JSON-формате.
# Минимальный базовый пример ответа - {"result": 10000}
class TokensTotalSupplyView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        contract_instance, block, gas_price, w3 = connect_smart_contract()
        # info about smart-contract
        name = contract_instance.functions.name().call()
        totalSupply = contract_instance.functions.totalSupply().call()
        info = [block,gas_price,name,totalSupply]
        
        return render(request, 'tokens/total_supply.html', {'info' : info, 'w3':w3})

# функция пре-создания контракта
def connect_smart_contract():
    # connect to eth
        w3 = Web3(Web3.HTTPProvider(settings.INFURA_PROJECT_ID))
        
        # variables from .env file
        address_contract = settings.ADDRESS_CONTRACT
        me = settings.ME
        abi = settings.ABI
        
        # прослойка между сетями
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        assert True is w3.isConnected()
        
        # info from blockchain      
        block = w3.eth.get_block('latest').number
        gas_price = w3.eth.gas_price
        
        # smart-contract
        contract_instance = w3.eth.contract(address=address_contract, abi=abi)
        
        # info about smart-contract
        name = contract_instance.functions.name().call()
        return contract_instance, block, gas_price, w3
