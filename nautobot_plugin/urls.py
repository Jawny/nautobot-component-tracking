from django.urls import path

from . import views

urlpatterns = [
        path('components', views.ComponentsView.as_view(), name='components'),
        ]
