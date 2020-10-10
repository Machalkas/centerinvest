from django.db import models

class Branch(models.Model):
    name=models.CharField(max_length=250, verbose_name='Название')
    addres=models.CharField(max_length=500, verbose_name='Адрес')
    discript=models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name, self.addres

class Services(models.Model):
    name=models.CharField(max_length=250, verbose_name='Услуга')
    window=models.IntegerField(verbose_name='Окно')
    branch=models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Queue(models.Model):
    time=models.TimeField(auto_now=False)
    service=models.ForeignKey('Services', on_delete=models.CASCADE)
    


