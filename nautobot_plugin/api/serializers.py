from rest_framework.serializers import ModelSerializer

from nautobot_plugin.models import Components

class ComponentsSerializer(ModelSerializer):
    class Meta:
        model = Components
        fields = ['name', 'description']
