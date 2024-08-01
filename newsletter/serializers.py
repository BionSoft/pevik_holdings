from rest_framework import serializers
from .models import newsletter

class newsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsletter
        fields = ['email', 'date_added']