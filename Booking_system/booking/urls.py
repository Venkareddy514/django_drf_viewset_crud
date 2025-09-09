
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('regions', RegionViewSet)
router.register('locations', LocationViewSet)
router.register('facilities', TestFacilityViewSet)
router.register('rooms', RoomViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = router.urls
