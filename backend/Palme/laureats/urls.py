from django.urls import path
from . import views

urlpatterns = [
      path('', views.accueil, name='acceuil'),
      path('laureats/', views.liste_laureats, name='liste_laureats'),
      path('supprimerl/<int:laureat_id>/', views.supprimer_laureat, name='supprimer_laureat'),
      path('modifier_laureat/<int:laureat_id>/', views.modifier_laureat, name='modifier_laureat'),
      path('films/', views.liste_films, name='liste_films'),
      path('supprimerf/<int:film_id>/', views.supprimer_film, name='supprimer_film'),
      path('modifier_film/<int:film_id>/', views.modifier_film, name='modifier_film'),
]