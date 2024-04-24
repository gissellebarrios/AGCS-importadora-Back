from rest_framework import serializers
from AGCS_importadora_Back.models import UserData, ProductoData, ClienteData, VentasData, ImportacionData
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','username','password']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class ClienteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteData
        fields = '__all__'

class ProductoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoData
        fields = '__all__'

class VentasDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentasData
        fields = '__all__'

class ImporDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportacionData
        fields = '__all__'

    