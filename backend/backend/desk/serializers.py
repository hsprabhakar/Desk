from rest_framework import serializers
from .models import Sticky

class StickySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticky
        fields = ('id', 'title', 'description', 'completed')