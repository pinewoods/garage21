from rest_framework import serializers

from .models import CylinderWeight

class CylinderWeightSerializer(serializers.ModelSerializer):
    channel = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CylinderWeight
        fields = ('channel', 'timestamp', 'unix_timestamp', 'sensor_reading')
