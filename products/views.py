from .models import Product
from rest_framework import viewsets, permissions, mixins
from .serializer import ProductSerializer


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    # permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

