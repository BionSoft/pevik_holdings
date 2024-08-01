from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'title', 'address', 'city', 'state', 'price', 'sale_type', 'property_type', 
            'bedrooms', 'bathrooms', 'sqft', 'property_size', 'video_file', 'video_url', 
            'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 
            'photo_6', 'photo_7', 'photo_8', 'photo_9', 'photo_10', 'photo_11', 
            'photo_12', 'photo_13', 'photo_14', 'photo_15', 'slug'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request is not None:
            for field in [
                'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 
                'photo_5', 'photo_6', 'photo_7', 'photo_8', 'photo_9', 
                'photo_10', 'photo_11', 'photo_12', 'photo_13', 'photo_14', 'photo_15']:
                photo = getattr(instance, field)
                if photo:
                    representation[field] = request.build_absolute_uri(photo.url)
        return representation

class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request is not None:
            for field in [
                'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 
                'photo_5', 'photo_6', 'photo_7', 'photo_8', 'photo_9', 
                'photo_10', 'photo_11', 'photo_12', 'photo_13', 'photo_14', 'photo_15']:
                photo = getattr(instance, field)
                if photo:
                    representation[field] = request.build_absolute_uri(photo.url)
        return representation
