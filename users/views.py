from django.contrib.auth.models import User
from solicitation.serializer import SolicitationSerializer

from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import UserSerializer

class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    # permission_classes = (permissions.DjangoModelPermissions, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def solicitations(self, request, pk=None):
        self.pagination_class.page_size = 5
        user = self.get_object()
        solicitations = user.solicitations.all()
        page = self.paginate_queryset(solicitations)

        if page is not None:
            serializer = SolicitationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)


        serializer = SolicitationSerializer(solicitations, many=True)
        return Response(serializer.data)
