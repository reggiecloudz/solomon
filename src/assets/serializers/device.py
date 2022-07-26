from rest_framework import serializers

from accounts.models import Client
from assets.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    open_requests = serializers.ReadOnlyField()
    request_count = serializers.ReadOnlyField()

    class Meta:
        model = Device
        fields = '__all__'
