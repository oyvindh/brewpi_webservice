from django.conf.urls import url, include

from rest_framework import routers

from .admin import admin_site
from .authentication import views as auth_views

router = routers.DefaultRouter()
router.register(r'auth/users', auth_views.UserViewSet)
router.register(r'auth/groups', auth_views.GroupViewSet)

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='BrewPI ReST API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', schema_view),
    url(r'^admin/', admin_site.urls),
]
