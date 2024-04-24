from rest_framework import serializers
from AGCS_importadora_Back.models import UserData
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','username','password']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id','nombre_completo','fecha_nacimiento','tipo_documento','nit','direccion','correo','telefono','rol']

    