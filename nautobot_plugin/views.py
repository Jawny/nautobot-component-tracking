from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ComponentsForm
from .models import Components

class ComponentsView(View):
    def get(self, request):
        components = Components.objects.all()
        return render(request, 'nautobot_plugin/components.html', {
            'components': components
        })

def add_component(request):
    """
    View for adding a new device.
    """
    if request.method == "POST":
        form = ComponentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/plugins/components/components")  # Redirect to the components view after successful form submission
    else:
        form = ComponentsForm()

    return render(request, "nautobot_plugin/add_component.html", {"form": form})
