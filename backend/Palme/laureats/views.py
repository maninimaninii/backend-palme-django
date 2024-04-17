from django.shortcuts import redirect, render
from .models import P09Laureat, P09Recompenserlaureat, P09Prix

def liste_laureats(request):
    laureats = P09Laureat.objects.all()
    laureats_list = []
    for laureat in laureats:
        recompenses = P09Recompenserlaureat.objects.filter(idlaureat=laureat.idlaureat)
        for recompense in recompenses:
            prix = P09Prix.objects.get(idprix=recompense.idprix)
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