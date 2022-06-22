from django.db import models

# Create your models here.
# class Login(models.Model):
#     login = models.CharField(verbose_name='Логин', max_length=20)
#     password = models.CharField(verbose_name='Пароль', max_length=32)
#     human_name = models.CharField(verbose_name='Имя', max_length=32)
#     human_family = models.CharField(verbose_name='Фамилия', max_length=32)
#     human_otchestvo = models.CharField(verbose_name='Отчество', max_length=32)
#     date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
#     date_update = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now=True)

#     def __str__(self):
#         return self.human_family

#     class Meta:
#         verbose_name = 'Учетные записи'
#         verbose_name_plural = 'Учетные записи'

# class NameChannel(models.Model):
#     name_channel = models.CharField(max_length=255)
#     id_human = models.ForeignKey(to='Login', on_delete=models.PROTECT)