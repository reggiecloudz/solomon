from rest_framework import serializers

from accounts.models import Client
from assets.models import Device

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'
