from django.db import models

class NivelEscolaridad(models.Model):
    NIVELES = [
        ('9no', '9° Grado'),
        ('tm', 'Técnico Medio'),
        ('12mo', '12° Grado'),
        ('uni', 'Universitario'),
    ]
    descripcion = models.CharField(max_length=255, choices=NIVELES)
    
    def __str__(self):
        return self.descripcion

class CategoriaDocente(models.Model):
    CATEGORIAS = [
        ('instructor', 'Instructor'),
        ('asistente', 'Asistente'),
        ('auxiliar', 'Auxiliar'),
        ('titular', 'Titular'),
    ]
    descripcion = models.CharField(max_length=255, choices=CATEGORIAS)
    
    def __str__(self):
        return self.descripcion

class CategoriaCientifica(models.Model):
    CATEGORIAS = [
        ('master', 'Máster'),
        ('doctor', 'Doctor'),
    ]
    descripcion = models.CharField(max_length=255, choices=CATEGORIAS)
    
    def __str__(self):
        return self.descripcion


class Trabajador(models.Model) :
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    carnet_identidad = models.IntegerField(default = 0)
    direccion = models.TextField()
    nivel_escolaridad = models.ForeignKey(NivelEscolaridad, on_delete=models.PROTECT)
    categoria_docente = models.ForeignKey(CategoriaDocente, on_delete=models.SET_NULL, null=True, blank=True)
    categoria_cientifica = models.ForeignKey(CategoriaCientifica, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
    
    def __str__(self):
        return self.nombre
    
    
    
    



