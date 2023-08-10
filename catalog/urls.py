from django.urls import path
from catalog.views import home, contact, product
from catalog.apps import CatalogConfig
# вызов функции при получении определенного запроса

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact'),
    path('product/', product, name='product')
]
