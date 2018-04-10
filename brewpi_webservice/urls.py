from django.conf.urls import url, include

from rest_framework_nested import routers

from .admin import admin_site

from authentication import views as auth_views
from controller import views as controller_views

router = routers.SimpleRouter()
router.register(r'auth/users', auth_views.UserViewSet)
router.register(r'auth/groups', auth_views.GroupViewSet)
router.register(r'controllers', controller_views.ControllerViewSet)

controller_router = routers.NestedSimpleRouter(router, r'controllers', lookup='controller')
controller_router.register(r'devices', controller_views.DeviceViewSet, base_name='device')

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='BrewPI ReST API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(controller_router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', schema_view),
    url(r'^admin/', admin_site.urls),
]
