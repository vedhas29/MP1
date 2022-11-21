from rest_framework import serializers
from .models import rooms
from .models import room_state


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = rooms
        fields = '__all__'


class RoomStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = room_state
        fields = '__all__'
  