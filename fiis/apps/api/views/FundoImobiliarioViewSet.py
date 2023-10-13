from fiis.apps.api.serializers import FundoImobiliarioSerializer
from rest_framework import viewsets, permissions
from fiis.apps.api.models import FundoImobiliario


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permission_classes = [permissions.IsAuthenticated]