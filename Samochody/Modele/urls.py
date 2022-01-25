from django.urls import include, path
from rest_framework import routers
from .views import ModeleViewSet

router = routers.DefaultRouter()
router.register(r'modeles', ModeleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namesspace="rest_framework"))
]