from operator import mod
from pyexpat import model
from sqlite3 import Date
from django.db import models

# Create your models here.

class Cliente(models.Model):
    GENEROS_CHOICES = [
       ('M', 'Masculino'),
       ('F', 'Femenino'),
       ('O', 'Otros'),
   ]
    documento = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    contacto = models.IntegerField()
    correo_electronico = models.CharField(max_length=70)
    genero = models.CharField(max_length=3, choices=GENEROS_CHOICES)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()

# class Usuario(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     password = models.CharField(max_length=64)

# class Planes(models.Model):
#     PLANES_CHOICES = [
#        ('M', 'Musculacion'),
#        ('Z', 'Zumba'),
#        ('F', 'Funcional'),
#        ('MZ', 'Musculacion y Zumba'),
#        ('MF', 'Musculacion y Funcional'),
#        ('MZF', 'Musculacion + Zumba + Funcional'),

#    ]
#     nombre = models.CharField(max_length=100)
#     planes = models.CharField(max_length= 6, choices=PLANES_CHOICES)
#     monto = models.IntegerField

# class Promocion(models.Model):
#     planes = models.ForeignKey(Planes, on_delete=models.CASCADE)
#     promocion = models.CharField(max_length=100)

# class Pagos(models.Model):
#     PAGOS_CHOICES = [
#        ('TC', 'Tarjeta de Credito'),
#        ('TD', 'Tarjeta de Debito'),
#        ('E', 'Efectivo'),
#        ('T', 'Transferencia Bancaria'),
#    ]
#     planes = models.ForeignKey(Planes, on_delete=models.CASCADE)
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     fecha = models.DateField
#     Tipo_pago = models.CharField(max_length= 4, choices=PAGOS_CHOICES)

# class Facturas(models.Model):
#     pago = models.ForeignKey(Pagos, on_delete=models.CASCADE)
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     planes = models.ForeignKey(Planes, on_delete=models.CASCADE)
#     nro_factura = models.BigAutoField
#     descripcion = models.CharField(max_length=200)
#     cantidad = models.IntegerField
#     iva = models.CharField(max_length=40)
#     fecha = models.DateField
#     sub_total = models.BigIntegerField
#     total = models.BigIntegerField

# class Inscripcion(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     planes = models.ForeignKey(Planes, on_delete=models.CASCADE)
#     factura = models.ForeignKey(Facturas, on_delete=models.CASCADE)
#     fecha = models.DateField
