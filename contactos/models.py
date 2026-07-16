from django.db import models
from django.core.validators import RegexValidator

class Contacto(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    # Validación básica para asegurar que el teléfono solo contenga números
    telefono = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message="El teléfono solo debe contener números."
            )
        ]
    )

    def __str__(self):
        return self.nombre