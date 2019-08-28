from django.db import models


# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["order", "title"]
