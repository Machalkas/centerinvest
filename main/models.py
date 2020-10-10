from django.db import models

class Branch(models.Model):
    name=models.CharField(max_length=250, verbose_name='Название')
    addres=models.CharField(max_length=500, verbose_name='Адрес')
    discript=models.TextField(verbose_name='Описание')

    def __str__(self):
        template = '{0.name} {0.addres}'
        return template.format(self)

class Services(models.Model):
    name=models.CharField(max_length=250, verbose_name='Услуга')
    window=models.IntegerField(verbose_name='Окно')
    branch=models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Queue(models.Model):
    time=models.DateTimeField()
    service=models.ForeignKey('Services',verbose_name='Услуга' , on_delete=models.CASCADE)
    branch=models.ForeignKey('Branch', on_delete=models.CASCADE, verbose_name='Фелиал', null=True, blank=True)
    number=models.CharField(max_length=5, verbose_name='Номер в очереди', null=True, blank=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.time



