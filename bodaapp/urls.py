from django.urls import path, include
from bodaapp.views import PersonnelViewSet, ShipperViewSet, CarrierViewSet, VehicleTypeViewset, VehicleViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('personnels', PersonnelViewSet, basename="personnels")
router.register('shippers', ShipperViewSet, basename='shippers')
router.register('carriers', CarrierViewSet, basename='carriers')
router.register('vehicletypes', VehicleTypeViewset, basename='vehicletypes')
router.register('vehicles', VehicleViewset, basename='vehicles')

urlpatterns = [
    path('', include(router.urls))
]
