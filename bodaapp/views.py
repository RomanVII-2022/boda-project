from django.shortcuts import render
from bodaapp.serializers import PersonnelSerializer, ShipperSerializer, CarrierSerializer, VehicleTypeSerializer, VehicleSerializer, OrderSerializer
from bodaapp.models import Personnel, Shipper, Carrier, VehicleType, Vehicle, Order
from rest_framework import viewsets, status
from rest_framework.response import Response 

class PersonnelViewSet(viewsets.ModelViewSet):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()


class ShipperViewSet(viewsets.ModelViewSet):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ShipperSerializer(data=request.data)
        if serializer.is_valid():
            # shipper = Shipper(full_name = serializer.validated_data['full_name'], 
            #                   email = serializer.validated_data['email'], 
            #                   phone_number = serializer.validated_data['phone_number'], 
            #                   business_or_person = serializer.validated_data['business_or_person']
            #                   )
            # shipper.set_password(serializer.validated_data['password'])
            # shipper.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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
