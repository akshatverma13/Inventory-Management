from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"suppliers", SupplierViewSet, basename="supplier")

urlpatterns = router.urls
