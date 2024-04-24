from django.db import models

# Create your models here.

class UserData(models.Model):
    nombre_completo = models.CharField(max_length=100, null= False, blank= True)
    fecha_nacimiento = models.DateField(null=False, blank= True)
    tipo_documento = models.CharField(max_length=50, null=False, blank= True)
    nit = models.CharField(max_length=20, null=False, blank= True)
    direccion = models.CharField(max_length=255, null=False, blank= True)
    telefono = models.CharField(max_length=20, null=False, blank= True)
    rol = models.CharField(max_length=20, null=False, blank= True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_completo
    
