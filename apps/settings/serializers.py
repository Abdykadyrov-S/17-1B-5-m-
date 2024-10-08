from rest_framework import serializers

from .models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title'] 
        # fields = '__all__' 
        # fields = ['id', 'title', 'logo', 'description'] 

class SettingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__' 

