from django.urls import path
from .views import RestauranteListView, RestauranteDetailView, reservasView, reservasView1, MenuView, ReservaMenuListView
from . import views

urlpatterns = [
    # path('', views.lista, name='listado'),
    path('', RestauranteListView.as_view(), name='listado'),
    path('resturantes/<int:pk>/', RestauranteDetailView.as_view(), name='detalles'),
    # path('resturantes/<int:pk>/',views.detalles, name='detalles'),
   # path('detalles/',reservasCreate.as_view(), name='NuevaReserva'),
    path('gracias/', views.gracias, name='gracias'),
    path('personas/', ReservaMenuListView.as_view(), name='menu1'),
    path('menu/<int:pk>', MenuView.as_view(), name='menu'),
    path( 'final/', reservasView.as_view(), name='final'),
    path('final1/', reservasView1.as_view(), name='final1'),
    path('pago/', views.pago, name='pago')
]
