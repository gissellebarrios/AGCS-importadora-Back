# Generated by Django 5.0.4 on 2024-04-24 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_nombre_cliente', models.CharField(blank=True, max_length=100)),
                ('cl_tipo_documento', models.IntegerField(choices=[(0, 'Cedula'), (1, 'Cedula de Extranjeria'), (2, 'Permiso Especial de Permanencia'), (3, 'Pasaporte'), (4, 'Nit')], default=0)),
                ('cl_nit', models.CharField(blank=True, max_length=20)),
                ('cl_telefono', models.CharField(blank=True, max_length=10)),
                ('cl_ciudad', models.CharField(blank=True, max_length=50)),
                ('cl_direccion', models.CharField(blank=True, max_length=50)),
                ('cl_correo', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_nombre_producto', models.CharField(blank=True, max_length=20)),
                ('pr_foto_producto', models.ImageField(blank=True, upload_to='')),
                ('pr_precio', models.CharField(blank=True, max_length=100)),
                ('pr_fecha_compra', models.DateField(blank=True)),
                ('pr_estado', models.IntegerField(choices=[(0, 'VENDIDO'), (1, 'DISPONIBLE'), (2, 'AGOTADO'), (3, 'POR VERIFICACION')], default=0)),
                ('pr_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Productocliente', to='AGCS_importadora_Back.clientedata')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(blank=True, max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('tipo_documento', models.CharField(blank=True, max_length=50)),
                ('nit', models.CharField(blank=True, max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=255)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('rol', models.CharField(blank=True, max_length=20)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='VentasData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vn_estado', models.IntegerField(choices=[(0, 'COMPLETA'), (1, 'ANULADA'), (2, 'CANCELADA'), (3, 'POR VERIFICACION')], default=3)),
                ('vn_fecha_venta', models.DateField(blank=True)),
                ('vn_producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='VentaProducto', to='AGCS_importadora_Back.productodata')),
                ('vn_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='VentaUsuario', to='AGCS_importadora_Back.userdata', to_field='usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ImportacionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imp_estado', models.IntegerField(choices=[(0, 'COMPLETA'), (1, 'ANULADA'), (2, 'CANCELADA'), (3, 'POR VERIFICACION')], default=3)),
                ('imp_fecha', models.DateField(blank=True)),
                ('imp_cantidad', models.IntegerField(blank=True)),
                ('imp_producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ImportacionProducto', to='AGCS_importadora_Back.productodata')),
                ('imp_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ImportacionUsuario', to='AGCS_importadora_Back.userdata', to_field='usuario')),
                ('imp_venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ImportacionVenta', to='AGCS_importadora_Back.ventasdata')),
            ],
        ),
    ]