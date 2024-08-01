from rest_framework import serializers
from .models import RealtorWaitlist

class RealtorWaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtorWaitlist
        fields = '__all__'