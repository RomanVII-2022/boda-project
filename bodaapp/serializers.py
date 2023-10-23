from rest_framework import serializers
from bodaapp.models import Personnel, Shipper, Carrier, VehicleType, Vehicle, Order

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        personel = Personnel(
            email = validated_data['email'],
            full_name = validated_data['full_name'],
            phone_number = validated_data['phone_number'],
            job_title = validated_data['job_title']
        )

        personel.set_password(validated_data['password'])
        personel.save()

        return personel

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'