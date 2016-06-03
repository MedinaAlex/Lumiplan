Réenregistrer le fichier source avant utilisation de l'application.

Ouvrez un fichier qui est généré par le template de base de squash pour les cas de test.

Ne pas mettre 2 fiches avec le même nom dans un projet (Erreur de Key dans le dictionnaire sinon).

Ne pas mettre de chevron ou de caractère & en dehors des Actions, des résultats, des exigences et des pré-requis.

Ne pas mettre de nom de fiche avec des guillemets.

Dans Squash, pour la description des fiches, ne pas faire de saut de ligne vide.



Dictionnaire sous la forme:

dictionnaire = {

	'general': [Liste des éléments sélectionnés dans l'ihm qui ont pour père 'general'. List of String],

	'num': [Liste de 1 jusqu'au nombre de fiches, List of Integer],

	'Other': [
		{
			'Pre-requis': RichText(String), 'Exigences': RichText(String)
		}
		...
	List of Dict]

	'is_Etape': Boolean

	'is_Statut': Boolean

	'Fiches': [
		{
			'Titre': String, 'Parent': String, 'ID': Integer, 'Description': String, 'Cree': String, 'Modifie': String,
			'Nature': String, 'Type': String, 'Statut': String, 'Importance': String, 'Jalons': String,
			'is_children': Boolean, 'other_father': Boolean
			'Etapes': [
				{
					'Numero': RichText(Integer), 'Action': RichText(String), 'Resultat': RichText(String)
				},
				...
			List of Dict],
		},
		...
	List of Dict]
}

voir le fichier /template/how_to_use.docx pour voir les différentes utilisations possible.
Voir la documentaion complète de [docxtpl](http://docxtpl.readthedocs.io/en/latest/)