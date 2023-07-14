from django.shortcuts import render
from django.views.generic import View

from .models import Components

class ComponentsView(View):
    def get(self, request):
        components = Components.objects.all()
        return render(request, 'nautobot_plugin/components.html', {
            'components': components
        })
