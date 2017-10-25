from django.conf.urls import include, url
from rest_framework import routers
from users import views as users_views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'groups', users_views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
