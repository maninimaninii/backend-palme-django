from django.shortcuts import redirect, render
from .models import P09Laureat, P09Recompenserlaureat, P09Prix, P09Film, P09Recompenserfilm

def liste_laureats(request):
    laureats = P09Laureat.objects.all()
    laureats_list = []
    for laureat in laureats:
        recompenses = P09Recompenserlaureat.objects.filter(idlaureat=laureat.idlaureat) #les recompenes associées au lauréat (possiblement plusieurs par laureat)
        for recompense in recompenses:
            prix = P09Prix.objects.get(idprix=recompense.idprix) #pour chaque recompense les infos du prix concerné
            laureats_list.append({
                "idLaureat" : laureat.idlaureat,
                "NomLaureat": laureat.nomlaureat,
                "Sexe": laureat.sexe,
                "Pays": laureat.pays,
                "Métier": laureat.metier,
                "EditionPrix": recompense.editionprixl,
                "NomPrix": prix.nomprix
            })
    return render(request, 'laureats/liste_laureats.html', {'laureats': laureats_list})



def supprimer_laureat(request, laureat_id):
    laureat = P09Laureat.objects.get(idlaureat=laureat_id)
    laureat.delete()
    return redirect('liste_laureats')






def supprimer_film(request, film_id):
    film = P09Film.objects.get(idfilm=film_id)
    film.delete()
    return redirect('liste_films')




def accueil(request):
    return render(request, 'laureats/accueil.html')



def liste_films(request):
    films = P09Film.objects.all()
    films_list = []
    for film in films : 
        recompenses = P09Recompenserfilm.objects.filter(idfilm = film.idfilm)
        for recompense in recompenses : 
            prix = P09Prix.objects.get(idprix = recompense.idprix) 
            real = P09Laureat.objects.get(idlaureat = film.idrealisateur) #on recupere l'utilisateur du film
            films_list.append({
                "idFilm" : film.idfilm,
                "NomFilm": film.titrefilm,
                "NomRealisateur" : real.nomlaureat,
                "Pays": film.paysfilm,
                "EditionPrix": recompense.editionprixf,
                "NomPrix": prix.nomprix
            })
    return render(request, 'laureats/liste_films.html', {'films': films_list})


