from django.conf.urls import url,include
from . import views

urlpatterns = [

    # Apartado Login
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),

    # Apartado Circunscripcion
    url(r'^circunscripcion/$', views.CircunscripcionLista.as_view(), name='circunscripcion_url'),
    url(r'^circunscripcion/crear/$', views.CircunscripcionCrear.as_view(), name='circunscripcion_crear_url'),
    url(r'^circunscripcion/vistaDetallada/(?P<pk>.*)$', views.CircunscripcionDetalle.as_view(), name='circunscripcion_detalle_url'),
    url(r'^circunscripcion/editar/(?P<pk>.*)$', views.CircunscripcionEditar.as_view(), name='editar_url'),
    url(r'^circunscripcion/eliminar/(?P<pk>.*)$', views.CircunscripcionEliminar.as_view(), name='eliminar_url'),

    # Apartado Mesa
    url(r'^mesa/$', views.MesaLista, name='mesa_url'),
    url(r'^mesa/vistaDetalladaMesa/(?P<pk>.*)$', views.MesaDetalle, name='mesa_detalle_url'),
    url(r'^mesa/crear/$', views.MesaCrear, name='mesa_crear_url'),
    url(r'^mesa/editar/(?P<pk>.*)$', views.MesaEditar, name='mesa_editar_url'),

    # Apartado Resultado
    url(r'^resultado/$', views.ResultadoLista.as_view(), name='resultado_url'),
    url(r'^resultado/crear/$', views.ResultadoCrear.as_view(), name='resultado_crear_url'),
]
