Réenregistrer le fichier source avant utilisation de l'application.

Ouvrez un fichier qui est généré par le template de base de squash pour les cas de test.

Ne pas mettre 2 fiches avec le même nom dans un projet



Dictionnaire sous la forme:

dictionnaire = {
	'general': [Liste des éléments sélectionnés dans l'ihm sui ont pour père 'general'. List of String],

	'NUM': [Liste de 0 au nombre de fiches, List of Integer],

	'Other': [
		{
			'Titre': RichText(String), 'Pre-requis': RichText(String), 'Exigences': RichText(String)
		}
		...
	]

	'Fiches': [
		{
			'Titre': String, 'ID': Integer, 'Description': String, 'Cree': String, 'Modifie': String,
			'Nature': String, 'Type': String, 'Statut': String, 'Importance': String, 'Jalons': String,
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