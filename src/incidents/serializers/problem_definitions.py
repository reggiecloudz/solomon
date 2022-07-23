from rest_framework import serializers

from incidents.models import ProblemDefinition

class ProblemDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemDefinition
        fields = '__all__'