from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet)
# router.register("sign/")
# router.register("login/")