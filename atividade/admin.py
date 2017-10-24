from django.contrib import admin
from .models import Perfil, Post, Contato, Comentario

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    model = Perfil
    list_display = ('persona', 'fotografia')

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('autor', 'titulo', 'texto', 'resumen',
              'imagenes', 'genero', 'fecha_creacion', 'fecha_publicacion')
    list_filter = ('autor', 'genero', 'fecha_creacion')
    save_on_top = True

class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = ('nome', 'email', 'texto', 'data')
    save_on_top = True

class ComentarioAdmin(admin.ModelAdmin):
    model = Comentario
    list_display = ('autor', 'email', 'url', 'texto', 'fecha')
    list_filter = ('autor', 'url', 'fecha')
    save_on_top = True



admin.site.register(Perfil, admin_class=PerfilAdmin)
admin.site.register(Post, admin_class=PostAdmin)
admin.site.register(Contato, admin_class=ContatoAdmin)
admin.site.register(Comentario,admin_class=ComentarioAdmin)
