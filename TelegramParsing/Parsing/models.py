from django.db import models

# Create your models here.
class Chanel(models.Model):
    NameChanel = models.CharField(verbose_name='Название канала', max_length=20)

    def __str__(self):
        return self.NameChanel