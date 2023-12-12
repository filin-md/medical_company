from django.db import models

# Create your models here.


class Analysis(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название анализа')
    description = models.TextField(verbose_name='Описание анализа')
    duration = models.PositiveIntegerField(verbose_name='Срок оказания услуги')
    price = models.PositiveIntegerField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'


class Doctor(models.Model):
    photo = models.ImageField(upload_to='photo/', verbose_name='Фото', null=True, blank=True)
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    profile = models.CharField(max_length=150, verbose_name='Медицинское направление')
    experience = models.PositiveSmallIntegerField(verbose_name='Стаж работы')
    start_price = models.PositiveIntegerField(verbose_name='Стоимость приёма')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Order(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    consultation_date = models.DateTimeField(verbose_name='Дата записи')
    client = models.CharField(max_length=150, verbose_name='ФИО клиента')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'



