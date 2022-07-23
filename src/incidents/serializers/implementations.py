from rest_framework import serializers

from incidents.models import Implementation

class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = '__all__'
