from .models import *
from rest_framework import serializers
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = "__all__"