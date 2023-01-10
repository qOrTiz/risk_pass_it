from rest_framework import serializers
from .models import *


class RiskSerializer(serializers.ModelSerializer):
    #image = serializers.CharField(source='image_1')

    class Meta:
        model = Risk
        depth = 1
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    #image = serializers.CharField(source='image_1')

    class Meta:
        model = Assessment
        depth = 1
        fields = '__all__'


class CountermeasuresSerializer(serializers.ModelSerializer):
    #image = serializers.CharField(source='image_1')

    class Meta:
        model = Countermeasures
        depth = 1
        fields = '__all__'


class DashboardSerializer(serializers.ModelSerializer):
    #image = serializers.CharField(source='image_1')

    class Meta:
        model = Dashboard
        depth = 1
        fields = '__all__'