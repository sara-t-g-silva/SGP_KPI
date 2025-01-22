from rest_framework import serializers
from .models import (
    Rpa_model, 
    Log_rpa_model, 
    Log_rpa_error_model)




class RpaSerializer(serializers.ModelSerializer):
    class   Meta:
        model= Rpa_model
        fields = '__all__'
        

class Log_rpaSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Log_rpa_model
        fields = '__all__'


class Log_rpa_error_model_serializer(serializers.ModelSerializer):
    class   Meta:
        model = Log_rpa_error_model
        fields = '__all__'
