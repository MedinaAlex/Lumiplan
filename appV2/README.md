# Règles d'utilisation
Dans Squash:
- Ne pas mettre 2 fiches avec le même nom dans un projet (Erreur de Key dans le dictionnaire sinon).
- Ne pas mettre de chevron ou de caractère & en dehors des Actions, des résultats, des exigences et des pré-requis.
- Évitez de mettre des noms de fiche avec des guillemets.
- Ne pas faire de saut de ligne vide dans la description des fiches.

# Utilisation de l'appication

- Réenregistrez le fichier source avant utilisation de l'application (le fichier ne doit pas faire plus de 500ko).
- Lancez *ihm.exe*.
- Ouvrez un fichier qui est généré par le template de base de squash pour les cas de test.
- Ouvrez votre template.
- Sélectionnez où enregistrer le fichier.

# Modification du code source
Les librairies *docx*, *docxtpl* sont nécéssaires en cas de modification.

# Regénérer l'exe
la librairie *py2exe* est nécessaire.
le script *setup.py* est utilisé pour créer l'exécutable
```
python setup.py py2exe
```
Un dossier *dist* et *build* vont être créés, vous pouvez supprimer *build*. L'exe est *ihm.exe* se trouvant dans le dossier *dist*.

## Détail sur les styles

### Le gras et l'italic
Les styles (gras, italic, puces) n'ont pas pu être gardés lors de la génération. Il existe un moyen d'ajouter ces styles dans les documents.

Cependant, je n'ai pas trouver de moyen de l'implémenter pour que ce soit simple d'utilisation. En effet grâce au *RichText*
de *docxtpl*, on peut ajouter des styles, cependant, étant donné la façon dont est généré mon dictionnaire (par paragraphe)
cela changerait le style de tout le paragraphe, il faudrait penser à une implémentation selon les *runs* des *paragraphes*.

Cela ne pourrait être nécessaire pour les *actions* et les *résultats*, il faudrait prévoir une liste de *RichTest* selon les *runs*
ou uniquement lors d'un changement de style, il faudra donc modifier le template en ajoutant une boucle au niveau des *actions* et *résultats*.
Cela marche également pour les *pré-requis* et les *exigences*.

Pour accéder aux styles des runs regarder la [documentation](https://python-docx.readthedocs.io/en/latest/api/text.html#docx.text.run.Run)


#### Exemple
Avec un document ouvert avec la librairie *docx*
```Python
from docx import Document

document = Document
for paragraph in document.paragraphs:
    for run in paragraph.runs:
        print(run.bold)
```
Cela va renvoyer des *boolean* si la run est en **gras**.
Il faudra donc ajouter dans le dictionnaire pour une valeur *True* 

```Python
'Action': [
	RichText('some text in '),
	RichText('bold', bold=True)
	]
```

### Les listes à puces
Les listes à puces sont un style particulier: *List Paragraph*

### Exemple
Ces styles sont accésible par :
```Python
from docx import Document

document = Document
for paragraph in document.paragraphs:
    print(paragraph.style)
```

Il faudra donc ajouter dans le dictionnaire si c'est une liste à puce :
```Python
'Action': [
	RichText('une puce', style=List Paragraph),
	RichText('une deuxième puce', style=List Paragraph)
	]
```

### Variable accésible via le template

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

##### Voir le fichier */template/how_to_use.docx* pour consulter les différentes utilisations possible.

##### Voir la documentaion complète de [docxtpl](http://docxtpl.readthedocs.io/en/latest/)
