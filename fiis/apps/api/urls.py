from rest_framework.routers import DefaultRouter
from fiis.apps.api.views import FundoImobiliarioViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'fundos', FundoImobiliarioViewSet)

urlpatterns = router.urls
