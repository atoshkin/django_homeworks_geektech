from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=155),
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='наименование')
    descriptions = models.TextField(verbose_name='Описание')
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'КИНО'
        verbose_name_plural = 'КИНО'

class Review(models.Model):
    text = models.TextField(verbose_name='текст')
