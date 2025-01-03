from django.db import models

class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()



class Habito(models.Model):
    idhabito=models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="habitos")
    nombre_habito = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    meta_diaria = models.IntegerField(help_text="Cantidad diaria objetivo (e.g., horas, minutos)")
    fecha_creacion = models.DateTimeField(auto_now_add=True)                               


class Progreso(models.Model):
    idprogreso=models.AutoField(primary_key=True)
    idhabito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name="progresos")
    fecha = models.DateField()
    tiempo_realizado = models.PositiveIntegerField()  # Minutos realizados
    notas = models.TextField(blank=True, null=True)




class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="notificaciones")
    idhabito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name="notificaciones")
    hora = models.TimeField()
    fecha_programada = models.DateTimeField()
    frecuencia = models.CharField(max_length=50, choices=[('Diaria', 'Diaria'), ('Semanal', 'Semanal')])
    estado = models.BooleanField(default=True)  # Activa/Inactiva
    tiempo_realizado = models.PositiveIntegerField(null=True, blank=True)  # Minutos realizados



class Meta(models.Model):
    idhabito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name='metas')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    valor_meta = models.DecimalField(max_digits=5, decimal_places=2)  # Por ejemplo, 3.0 horas de estudio
    fecha_limite = models.DateField()
