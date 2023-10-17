from rest_framework import serializers
from bodaapp.models import Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'