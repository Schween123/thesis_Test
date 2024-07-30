from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, BoardingHouseViewSet, RoomViewSet, TenantViewSet, GuardianViewSet, TransactionViewSet, FaceImageViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'boardinghouses', BoardingHouseViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'guardians', GuardianViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'faceimages', FaceImageViewSet)

urlpatterns = router.urls
