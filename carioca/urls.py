from django.urls import path, include
from .views import TimesViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'times', TimesViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]
