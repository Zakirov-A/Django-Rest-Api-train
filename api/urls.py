from rest_framework import routers

from api.views import CarViewSet

router = routers.DefaultRouter()
router.register('car', CarViewSet)

urlpatterns = router.urls