from django.db import models
from django import forms

class ModifierFilmForm(forms.Form):
    titre = forms.CharField(label='Titre du film', max_length=140, widget=forms.TextInput(attrs={'class' : 'tit'}))
    pays = forms.CharField(label='Pays d\'origine du film', max_length=60, widget=forms.TextInput(attrs={'class' : 'tit'}))
    realisateur = forms.ChoiceField(label='Réalisateur')

    def __init__(self, *args, **kwargs):
        super(ModifierFilmForm, self).__init__(*args, **kwargs)
        # Récupérer les laureats dont le métier est réalisateur
        realisateurs = P09Laureat.objects.filter(metier='realisateur')
        # Créer une liste d'options pour le champ de sélection du réalisateur
        realisateur_choices = [(laureat.idlaureat, laureat.nomlaureat) for laureat in realisateurs]
        # Remplir le champ de sélection avec les options
        self.fields['realisateur'].choices = realisateur_choices



class P09Film(models.Model):
    idfilm = models.AutoField(db_column='idFilm', primary_key=True)  # Field name made lowercase.
    titrefilm = models.CharField(db_column='titreFilm', max_length=140)  # Field name made lowercase.
    paysfilm = models.CharField(db_column='paysFilm', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idrealisateur = models.IntegerField(db_column='idRealisateur')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'p09_film'


class P09Laureat(models.Model):
    idlaureat = models.AutoField(db_column='idLaureat', primary_key=True)  # Field name made lowercase.
    nomlaureat = models.CharField(db_column='nomLaureat', max_length=91)  # Field name made lowercase.
    sexe = models.CharField(max_length=10, blank=True, null=True)
    pays = models.CharField(max_length=60, blank=True, null=True)
    metier = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p09_laureat'


class P09Prix(models.Model):
    idprix = models.AutoField(db_column='idPrix', primary_key=True)  # Field name made lowercase.
    nomprix = models.CharField(db_column='nomPriX', max_length=91)  # Field name made lowercase.
    typeprix = models.CharField(db_column='typePrix', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'p09_prix'


class P09Recompenserfilm(models.Model):
    idfilm = models.IntegerField(db_column='idFilm', primary_key=True)  # Field name made lowercase. The composite primary key (idFilm, idPrix) found, that is not supported. The first column is selected.
    idprix = models.IntegerField(db_column='idPrix')  # Field name made lowercase.
    editionprixf = models.DateField(db_column='editionPrixF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'p09_recompenserfilm'
        unique_together = (('idfilm', 'idprix'),)


class P09Recompenserlaureat(models.Model):
    idlaureat = models.IntegerField(db_column='idLaureat', primary_key=True)  # Field name made lowercase. The composite primary key (idLaureat, idPrix) found, that is not supported. The first column is selected.
    idprix = models.IntegerField(db_column='idPrix')  # Field name made lowercase.
    editionprixl = models.DateField(db_column='EditionPrixL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'p09_recompenserlaureat'
        unique_together = (('idlaureat', 'idprix'),)
