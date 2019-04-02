import logging
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from apps.products.models import Product
from apps.products.api.serializers import ProductListSerializer
from apps.products.api.filters import ProductFilter
logger = logging.getLogger('django')

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination
    filter_class = ProductFilter

    def get(self, *args, **kwargs):
        print('asdasdasd')
        logger.debug('Something went wrong!')
        return super().get(*args, **kwargs)

#http://127.0.0.1:8000/products/all/?page=3&perPage=96
#http://127.0.0.1:8000/products/all/?limit=192&offset=192

