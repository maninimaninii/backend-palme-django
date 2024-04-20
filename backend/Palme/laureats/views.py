from django.shortcuts import redirect, render
from .models import P09Laureat, P09Recompenserlaureat, P09Prix, P09Film, P09Recompenserfilm, ModifierFilmForm, ModifierLaureatForm,AjouterFilmForm, AjouterLaureatForm

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
    return render(request, 'films/liste_films.html', {'films': films_list})




def modifier_film(request, film_id):
    film = P09Film.objects.get(idfilm=film_id)
    if request.method == 'POST':  #formulairee soumis
        form = ModifierFilmForm(request.POST)
        if form.is_valid():
            film.titrefilm = form.cleaned_data['titre']
            film.paysfilm = form.cleaned_data['pays']
            film.idrealisateur = form.cleaned_data['realisateur']
            film.save()
            # redirection liste car modification finie
            return redirect('liste_films')
    else: #on cree le formulaire avec les infos préremplies depuis le film à modifier 
        form = ModifierFilmForm(initial={'titre': film.titrefilm, 'pays': film.paysfilm, 'realisateur': film.idrealisateur})
    return render(request, 'films/modifier_film.html', {'form': form}) #on renvoie la page de modification





def ajouter_film(request):
    if request.method == 'POST':
        form = AjouterFilmForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            pays = form.cleaned_data['pays']
            realisateur_id = form.cleaned_data['realisateur']
            edition = form.cleaned_data['edition']
            prix = form.cleaned_data['prixgagne']
            
            # création du film dans la base de données
            film = P09Film.objects.create(
                titrefilm=titre,
                paysfilm=pays,
                idrealisateur=realisateur_id
            )

            filme = P09Film.objects.get(titrefilm = titre)
            recompense = P09Recompenserfilm.objects.create(
                idfilm = filme.idfilm,
                idprix = prix,
                editionprixf = edition
            )


            # redirection vers la liste des films après ajout
            return redirect('liste_films')
    else:
        form = AjouterFilmForm()
    
    return render(request, 'films/ajouter_film.html', {'form': form})





def ajouter_laureat(request):
    if request.method == 'POST':
        form = AjouterLaureatForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            pays = form.cleaned_data['pays']
            sexe = form.cleaned_data['sexe']
            metier = form.cleaned_data['metier']
            edition = form.cleaned_data['edition']
            prix = form.cleaned_data['prixgagne']
            
            # création du film dans la base de données
            laureat = P09Laureat.objects.create(
                nomlaureat=nom,
                pays=pays,
                sexe=sexe,
                metier = metier
            )

            filme = P09Laureat.objects.get(nomlaureat = nom)
            recompense = P09Recompenserlaureat.objects.create(
                idlaureat = filme.idlaureat,
                idprix = prix,
                editionprixl = edition
            )


            # redirection vers la liste des films après ajout
            return redirect('liste_laureats')
    else:
        form = AjouterLaureatForm()
    
    return render(request, 'laureats/ajouter_laureat.html', {'form': form})










def modifier_laureat(request, laureat_id):
    laureat = P09Laureat.objects.get(idlaureat=laureat_id)
    if request.method == 'POST':  #formulairee soumis
        form = ModifierLaureatForm(request.POST)
        if form.is_valid():
            laureat.nomlaureat = form.cleaned_data['nom']
            laureat.pays = form.cleaned_data['pays']
            laureat.metier = form.cleaned_data['metier']
            laureat.sexe = form.cleaned_data['sexe']
            laureat.save()
            
            # redirection liste car modification finie
            return redirect('liste_laureats')
    else: #on cree le formulaire avec les infos préremplies depuis le film à modifier 
        form = ModifierLaureatForm(initial={'nom': laureat.nomlaureat, 'pays': laureat.pays, 'metier': laureat.metier, 'sexe' : laureat.sexe})
    return render(request, 'laureats/modifier_laureat.html', {'form': form}) #on renvoie la page de modification



