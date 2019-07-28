from django.urls import path
from listado.views import RestauranteListView, RestauranteDetailView
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('info/', views.info, name='informacion'),
    path('final/', views.final, name='final'),
    #path('', buscar.as_view(), name='index'),
    # path('', views.Login, name='ingreso')
]
