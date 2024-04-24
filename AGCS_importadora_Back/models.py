from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   on_delete= models.CASCADE,
                                   default="",
                                   to_field="username")
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
    
class ClienteData(models.Model):
    TIPO_DOC_CHOICES = [
            (0, "Cedula"),
            (1, "Cedula de Extranjeria"),
            (2, "Permiso Especial de Permanencia"),
            (3, "Pasaporte"),
            (4, "Nit")
    ]
    cl_nombre_cliente = models.CharField(max_length=100, null= False, blank= True)
    cl_tipo_documento = models.IntegerField(choices= TIPO_DOC_CHOICES, default=0)
    cl_nit = models.CharField(max_length=20, null= False, blank= True)
    cl_telefono = models.CharField(max_length=10, null= False, blank= True)
    cl_ciudad = models.CharField(max_length=50, null= False, blank= True)
    cl_direccion = models.CharField(max_length=50, null= False, blank= True)
    cl_correo = models.EmailField(unique=True) 

    def __str__(self):
        return self.cl_nombre_cliente

class ProductoData(models.Model):
    ESTADO_COMPRA_CHOICES = [
        (0, "VENDIDO"),
        (1, "DISPONIBLE"),
        (2, "AGOTADO"),
        (3, "POR VERIFICACION"),
    ]
    pr_cliente = models.ForeignKey(ClienteData, related_name= "Productocliente", on_delete=models.DO_NOTHING, to_field="id")
    pr_nombre_producto = models.CharField(max_length=20, null= False, blank= True)
    pr_foto_producto = models.ImageField(upload_to= "", blank= True)
    pr_precio = models.CharField(max_length=100, null= False, blank= True)
    pr_fecha_compra = models.DateField(null=False, blank=True)
    pr_estado = models.IntegerField(choices=ESTADO_COMPRA_CHOICES, default=0)
    
    def __str__(self):
        return self.pr_nombre_producto
    
class VentasData(models.Model):
    ESTADO_VENTA_CHOICES = [
        (0, "COMPLETA"),
        (1, "ANULADA"),
        (2, "CANCELADA"),
        (3, "POR VERIFICACION"),
    ]
    vn_producto = models.ForeignKey(ProductoData, related_name="VentaProducto", on_delete=models.DO_NOTHING, to_field="id")
    vn_usuario = models.ForeignKey(UserData, related_name= "VentaUsuario", on_delete= models.DO_NOTHING, to_field="usuario")
    vn_estado = models.IntegerField(choices=ESTADO_VENTA_CHOICES, default=3)
    vn_fecha_venta = models.DateField(null=False, blank= True)

    def __str__(self):
        return self.vn_producto
    
class ImportacionData(models.Model):
    ESTADO_IMP_CHOICES = [
        (0, "COMPLETA"),
        (1, "ANULADA"),
        (2, "CANCELADA"),
        (3, "POR VERIFICACION"),
    ]
    imp_usuario = models.ForeignKey(UserData, related_name="ImportacionUsuario", on_delete= models.DO_NOTHING, to_field="usuario")
    imp_producto = models.ForeignKey(ProductoData, related_name="ImportacionProducto", on_delete=models.DO_NOTHING, to_field="id")
    imp_venta = models.ForeignKey(VentasData, related_name="ImportacionVenta", on_delete= models.DO_NOTHING, to_field="id")
    imp_estado = models.IntegerField(choices=ESTADO_IMP_CHOICES, default=3)
    imp_fecha = models.DateField(null=False, blank=True)
    imp_cantidad = models.IntegerField(null=False, blank= True)