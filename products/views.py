from rest_framework import generics
from .models import Product
from .seralizer import ProductSerializer
from .produser import publish
# Create your views here.

class ProductView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        publish()
        print("publish()",publish())
        return super().get_queryset()
    