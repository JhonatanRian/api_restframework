from rest_framework.routers import SimpleRouter
from .views import SolicitationViewSet, InvoiceAllAPIView

router = SimpleRouter()
router.register("solicitations", SolicitationViewSet)
