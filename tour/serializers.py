from rest_framework import serializers
from .models import Tour

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['name', 'email', 'phone_number', 'available_day', 'message']