from django.urls import path, include
from bodaapp.views import PersonnelViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('personnels', PersonnelViewSet, basename="personnels")

urlpatterns = [
    path('', include(router.urls))
]
