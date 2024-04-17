from django.urls import path
from . import views

urlpatterns = [
      path('', views.liste_laureats, name='liste_laureats'),
      path('supprimer/<int:laureat_id>/', views.supprimer_laureat, name='supprimer_laureat'),
]