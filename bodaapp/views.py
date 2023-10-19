from django.shortcuts import render
from bodaapp.serializers import PersonnelSerializer, ShipperSerializer, CarrierSerializer, VehicleTypeSerializer, VehicleSerializer, OrderSerializer
from bodaapp.models import Personnel, Shipper, Carrier, VehicleType, Vehicle, Order
from rest_framework import viewsets

class PersonnelViewSet(viewsets.ModelViewSet):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()


class ShipperViewSet(viewsets.ModelViewSet):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.all()


class CarrierViewSet(viewsets.ModelViewSet):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.all()


class VehicleTypeViewset(viewsets.ModelViewSet):
    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()


class VehicleViewset(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
