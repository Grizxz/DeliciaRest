from django.db import models
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType

class prueba (models.Model):
    id = models.AutoField(primary_key=True)
# Create your models here.

class Persona (models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    email = models.CharField(max_length=150)


class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    contrasenia= models.CharField(max_length=20)

class Genero(models.Model):
    idGenero = models.IntegerField()
    descripcion = models.CharField(max_length=150)

#Separación de roles
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField('Rol', max_length=50,unique= True)
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'
    def __str__(self):
        return self.rol
    def save(self,*args,**kwargs):
        permisos_defecto =['add','change','delete','view']
        if not self.id:
            nuevo_grupo,creado = Group.objects.get_or_create(name = f'{self.rol}')
            for permiso_temp in permisos_defecto:
                permiso,created = Permission.objects.update_or_create(
                    name = f'Can{permiso_temp} {self.rol}',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.rol}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
        super().save(*args,**kwargs)


class Reserva(models.Model):
    idReserva = models.IntegerField()
    fecha = models.DateField()
    hora = models.DateTimeField()

class Ingrediente(models.Model):
    idIngrediente = models.IntegerField()
    descripcion = models.CharField(max_length=150)

class plato(models.Model):
    idPlato = models.IntegerField()
    descripcion = models.CharField