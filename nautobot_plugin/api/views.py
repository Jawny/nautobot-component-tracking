from rest_framework.viewsets import ModelViewSet

from nautobot_plugin.models import Components
from .serializers import ComponentsSerializer

class ComponentsViewSet(ModelViewSet):
    queryset = Components.objects.all()
    serializer_class = ComponentsSerializer
