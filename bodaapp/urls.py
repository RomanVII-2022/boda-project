from django.urls import path, include
from bodaapp.views import PersonnelViewSet, ShipperViewSet, CarrierViewSet, VehicleTypeViewset, VehicleViewset, OrderViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('personnels', PersonnelViewSet, basename="personnels")
router.register('shippers', ShipperViewSet, basename='shippers')
router.register('carriers', CarrierViewSet, basename='carriers')
router.register('vehicletypes', VehicleTypeViewset, basename='vehicletypes')
router.register('vehicles', VehicleViewset, basename='vehicles')
router.register('orders', OrderViewset, basename='orders')

urlpatterns = [
    path('', include(router.urls))
]
