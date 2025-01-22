from rest_framework import serializers
from rpas.models import Rpa


class RpaSerializer (serializers.ModelSerializer):

    class Meta:
        model = Rpa
        fields = '__all__'
