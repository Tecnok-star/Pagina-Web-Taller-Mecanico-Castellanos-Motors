from django.db import models
from django.contrib.auth.models import User #se importa los modelos de ususarios

class Vehiculo(models.Model):
    MARCAS_CHOICES = [
        ('CHERY', 'Chery'),
        ('DONGFENG', 'Dongfeng'),
        ('TOYOTA', 'Toyota'),
        ('CHEVROLET', 'Chevrolet'),
        ('OTRA', 'Otra'),
    ]

    # ForeignKey vincula cada vehículo a un dueño (usuario)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20, choices=MARCAS_CHOICES)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=15, unique=True) # unique evita placas repetidas
    anio = models.IntegerField()

def __str__(self):
    return f"{self.marca} {self.modelo} - Placa: {self.placa}"

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    # El admin controla esta cantidad exacta
    cantidad_disponible = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} (Disponibles: {self.cantidad_disponible})"

class Cita(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo_servicio = models.TextField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f"Cita: {self.cliente.username} - {self.fecha_hora.strftime('%d/%m/%Y')}"

class Reparacion(models.Model):
    ESTADO_REP_CHOICES = [
        ('RECEPCION', 'En Recepción'),
        ('DIAGNOSTICO', 'En Diagnóstico'),
        ('EJECUCION', 'Trabajando'),
        ('LISTO', 'Listo para Entregar'),
    ]
    
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    descripcion_sistema = models.TextField(help_text="Registro para el administrador sobre el estado del sistema.")
    estado = models.CharField(max_length=20, choices=ESTADO_REP_CHOICES, default='RECEPCION')
    fecha_ingreso = models.DateField(auto_now_add=True) # Se llena solo al crear el registro
    fecha_salida = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Seguimiento: {self.vehiculo.placa} - {self.get_estado_display()}"