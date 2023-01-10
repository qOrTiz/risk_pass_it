from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from . import serializers


class RiskList(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = serializers.RiskSerializer


class AssessmentList(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = serializers.AssessmentSerializer


class CountermeasuresList(viewsets.ModelViewSet):
    queryset = Countermeasures.objects.all()
    serializer_class = serializers.CountermeasuresSerializer


class DashboardList(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = serializers.DashboardSerializer