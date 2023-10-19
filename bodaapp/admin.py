from django.contrib import admin
from bodaapp.models import Personnel, Shipper, Carrier, VehicleType, Vehicle, Order


admin.site.register(Personnel)
admin.site.register(Shipper)
admin.site.register(Carrier)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(Order)
