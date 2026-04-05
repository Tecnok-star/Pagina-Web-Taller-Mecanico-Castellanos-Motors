from django.contrib import admin
from .models import Vehiculo, Repuesto, Cita, Reparacion

# Registramos las clases para que aparezcan en el panel web
admin.site.register(Vehiculo)
admin.site.register(Repuesto)
admin.site.register(Cita)
admin.site.register(Reparacion)
