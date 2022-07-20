from .models import Solicitation, Finances
from products.models import Product
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, mixins, status
from .serializer import SolicitationSerializer, InvoiceSerializer, ProfitSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


class InvoiceAllAPIView(APIView):
    queryset = []
    serializer_class = InvoiceSerializer

    def get(self, request):
        invoice = Finances.objects.first()
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)


class ProfitAllAPIView(APIView):
    queryset = []
    serializer_class = ProfitSerializer

    def get(self, request):
        profit = Finances.objects.first()
        serializer = ProfitSerializer(profit)
        return Response(serializer.data)


class SolicitationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    # permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        solicitation = self.perform_create(request.data)
        serializer = SolicitationSerializer(solicitation)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, data):
        product = Product.objects.get(id=data["product"][0])
        user = User.objects.get(id=data["client"][0])
        finance = Finances.objects.first()
        price_product = product.price_in_sale
        amount = int(data["quantity"][0]) * int(price_product)

        solicitation = Solicitation.objects.create(
            product=product,
            client=user,
            quantity=data["quantity"][0],
            amount=amount,
            delivery_place=data["delivery_place"]
        )
        if finance == None:
            finance = Finances.objects.create()
        finance.invoice_all += amount
        regular = 0
        for solicit in Solicitation.objects.all():
            regular += int(solicit.quantity) * float(solicit.product.regular_price)
        finance.profit = float(finance.invoice_all) - float(regular)
        finance.save()
        return solicitation