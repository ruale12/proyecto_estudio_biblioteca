from django.db import models;

# Create your models here.

class Author(models.Model):
    name = models.CharField('nombre',max_length = 200);
    last_name = models.CharField('apellido',max_length = 200);
    nationality = models.CharField('nationalidad',max_length = 200);
    description = models.TextField('descripcion');

    class Meta:
        verbose_name = 'Author';
        verbose_name_plural = 'Authors';
        ordering = ["name"];

    def __str__(self):
        return self.name;
