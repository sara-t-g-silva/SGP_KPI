from rest_framework import serializers
from rpa_log_successes.models import RpaLogSuccess


class RpaLogSuccessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= RpaLogSuccess
        fields = '__all__'
