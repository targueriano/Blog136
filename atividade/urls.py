from django.conf.urls import include, url
from . import views


contactos_patterns = [
    url(
        regex=r'^$',
        view=views.Contactos.as_view(),
        name='contatos'
    ),
    url(
        regex=r'^exito/$',
        view=views.exito,
        name='exito'
    ),
]

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contactos/', include(contactos_patterns)),
    url(r'^post/(?P<pk>\d+)/$', views.post_detalhe, name='post_detalhe'),
    url(r'^category/(?P<cat>\w+)/$', views.category, name='category')
]
