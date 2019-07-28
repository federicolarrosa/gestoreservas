from django.urls import path
from .views import ReservaListView, ReservaDetailView, ReservaDeleteView
urlpatterns = [
   path('', ReservaListView.as_view(), name='reservas'),
   path('<int:pk>/', ReservaDetailView.as_view(), name='reserva-detalles'),
   path('<int:pk>/delete', ReservaDeleteView.as_view(), name='reserva-delete'),
   
]