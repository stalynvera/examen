from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} por {self.usuario}"

    def clean(self):
        # Validación para asegurar que la fecha de devolución sea posterior a la fecha de préstamo
        if self.fecha_devolucion and self.fecha_devolucion <= self.fecha_prestamo:
            raise ValidationError("La fecha de devolución debe ser posterior a la fecha de préstamo.")
        # Validación para asegurar que la fecha de préstamo no sea en el futuro
        if self.fecha_prestamo > timezone.now().date():
            raise ValidationError("La fecha de préstamo no puede ser en el futuro.")
