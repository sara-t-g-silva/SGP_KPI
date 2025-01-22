from rest_framework import serializers
from rpa_log_errors.models import RpaLogError


class RpaLogErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RpaLogError
        fields = '__all__'

    