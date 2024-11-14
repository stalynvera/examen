from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False) 
    apellido = models.CharField(max_length=100, blank=False)  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False) 
    apellido = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, blank=False) 
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)  
    fecha_prestamo = models.DateField(blank=False)  
    fecha_devolucion = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} por {self.usuario}"

    def clean(self):
       
        if self.fecha_devolucion and self.fecha_devolucion <= self.fecha_prestamo:
            raise ValidationError("La fecha de devolución debe ser posterior a la fecha de préstamo.")
        
       
        if self.fecha_prestamo > timezone.now().date():
            raise ValidationError("La fecha de préstamo no puede ser en el futuro.")
