#coding:UTF-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# Create your models here.
class Perfil(models.Model):
    persona = models.OneToOneField(User)
    fotografia = models.ImageField(upload_to='personas/')

    def __unicode__(self):
        return self.persona.username

    def __str__(self):
        return self.persona.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

class Post(models.Model):
    GER = (
        ('Medicina', 'Medicina'),
        (u'Computação',u'Computação'),
        (u'História', u'História'),
    )
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    resumen = models.TextField()
    imagenes = models.ImageField(upload_to='posts/')
    genero = models.CharField(max_length=20, choices=GER, default=GER[0])
    fecha_creacion = models.DateTimeField('Fecha de criación', default=timezone.now)
    fecha_publicacion = models.DateTimeField('Fecha de publicación', blank=True, null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post)
    autor = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField("Website", blank=True, null=True)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __unicode__(self):
        return self.autor

    def __str__(self):
        return self.autor
