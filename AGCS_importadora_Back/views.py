from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from AGCS_importadora_Back.models import UserData, ClienteData, ProductoData, VentasData, ImportacionData
from AGCS_importadora_Back.serializers import UserDataSerializer,UserLoginSerializer,ClienteDataSerializer, ProductoDataSerializer, VentasDataSerializer,ImporDataSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh':str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request, format = None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password = password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg':'Login success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_fields_errors':['User or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status= status.HTTP_400)

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClienteDataViewSet(viewsets.ModelViewSet):
    queryset = ClienteData.objects.all()
    serializer_class = ClienteDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoDataViewSet(viewsets.ModelViewSet):
    queryset = ProductoData.objects.all()
    serializer_class = ProductoDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class VentaDataViewSet(viewsets.ModelViewSet):
    queryset = VentasData.objects.all()
    serializer_class = VentasDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImporDataViewSet(viewsets.ModelViewSet):
    queryset = ImportacionData.objects.all()
    serializer_class = ImporDataSerializer
    permission_classes = [permissions.IsAuthenticated]