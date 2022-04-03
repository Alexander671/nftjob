from django.db import models
from django.conf import settings

#
#  id          - primary key
#  unique_hash - уникальный хэш
#  tx_hash     - хэш транзакции создания токена
#  media_url   - урл с произвольным изображением
#  owner       - адрес пользователя в сети Ethereum
#

# новый обьект модели Token, в который сохраняются данные из параметра запроса,
# помимо этого генерируется любая рандомная строка*,
# которая также сохраняется в созданный обьект. Объект сохраняется.
# Любая рандомная строка  - должна состоять из букв и цифр
# (т.е. без спецсимволов) и иметь длину в 20 знаков.

class Tokens(models.Model):
    unique_hash = models.CharField(max_length=20, unique=True) 
    tx_hash = models.CharField(max_length=30, unique=True)
    media_url = models.URLField()
    user = models.TextField() # mb hex type?
    description = models.TextField()
    class Meta:
        verbose_name = ("Token") 
        verbose_name_plural = ("Tokens")
    def __str__(self):
        return str(self.user)  # __str__ применяется для отображения объекта в интерфейсе
