from django.contrib import admin
from .models import Libro, Autor, Prestamo, Usuario

# Registrar los modelos en el panel de administración
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Prestamo)
admin.site.register(Usuario)
