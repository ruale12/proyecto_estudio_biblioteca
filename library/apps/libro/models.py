from django.db import models;

# Create your models here.

class Author(models.Model):
    name = models.CharField('nombre',max_length = 200);
    last_name = models.CharField('apellido',max_length = 200);
    nationality = models.CharField('nationalidad',max_length = 200);
    description = models.TextField('descripcion');
    create_date = models.DateField('fecha creacion', auto_now = True, auto_now_add = False);

    class Meta:
        verbose_name = 'Author';
        verbose_name_plural = 'Authors';
        ordering = ["name"];

    def __str__(self):
        return self.name;


class Book(models.Model):
    name = models.CharField('Nombre',max_length = 200);
    put_date = models.DateField("Fecha de publicacion");
    author_id = models.ManyToManyField(Author);
    create_date = models.DateField('fecha creacion', auto_now = True, auto_now_add = False);
    
    class Meta:
        verbose_name = 'Book';
        verbose_name_plural = 'Books';
        ordering = ["name"];

    def __str__(self):
        return self.name;
