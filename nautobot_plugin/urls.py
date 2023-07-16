from django.urls import path

from . import views

urlpatterns = [
        path('components', views.ComponentsView.as_view(), name='components'),
        path('add_component', views.add_component, name='add_component'),
        ]
