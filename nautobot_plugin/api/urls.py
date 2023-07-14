from rest_framework import routers

from .views import ComponentsViewSet

router = routers.DefaultRouter()
router.register('components', ComponentsViewSet)
urlpatterns = router.urls
