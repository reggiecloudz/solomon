from rest_framework import serializers

from incidents.models import RootCause

class RootCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RootCause
        fields = '__all__'
