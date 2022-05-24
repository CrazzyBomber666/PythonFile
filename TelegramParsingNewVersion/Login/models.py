from django.db import models

# Create your models here.
class Login(models.Model):
    login = models.CharField(verbose_name='Логин', max_length=20)
    password = models.CharField(verbose_name='Пароль', max_length=32)
    human_name = models.CharField(verbose_name='Имя', max_length=32)
    human_family = models.CharField(verbose_name='Фамилия', max_length=32)
    human_otchestvo = models.CharField(verbose_name='Отчество', max_length=32)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.human_name + ' ' + self.human_family + ' ' + self.human_otchestvo + ' ' + self.date_create + ' ' + self.date_update

    class Meta:
        verbose_name = 'Учетные записи'
        verbose_name_plural = 'Учетные записи'