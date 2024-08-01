from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'id', 'address', 'price', 'project_type', 'units','featured','phone', 'project_logo', 'photo_1', 'photo_2', 'photo_3', 'photo_4','photo_5', 'video_photo', 'video','video_url','extimated_price', 'list_date', 'slug')

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        lookup_field = 'slug'