from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StickySerializer
from .models import Sticky

# Create your views here.

class StickyView(viewsets.ModelViewSet):
    serializer_class = StickySerializer
    queryset = Sticky.objects.all()