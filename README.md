# Présentation du stage
Le stage chez Lumiplan consiste à réaliser un outil de traitement plus ou moins automatique 
des documents word fourni par SquashTm, un gestionnaire de référentiel de test. En effet, 
les documents de sorties de SquashTm ont une mise en forme qui n'est pas adaptée pour 
une présentation aux clients de Lumiplan.

Je dois donc réaliser diverse opérations qui permettra d'avoir une mise en forme des documents convenable.

Je dois par ailleurs permettre aux utilisateurs de cet outil, de créer de nouveau document selon des templates
en sélectionnant des extraits depuis d'autre fichiers.

Il y a aussi du travail à réaliser sur un serveur où se trouve la base de donnée de SquashTm, je dois mettre à jour Squash ainsi que la base de donnée.

Pour ne pas travailler directement sur le serveur, j'utilise une machine virtuelle Debian, sur laquelle j'ai récupéré la base de donnée du serveur.

Il peut y avoir des changements dans les objectifs de ce stage selon la complexité de résolution de celui-ci.

### L'application

L'application finale se trouve dans le dossier [appV2](https://github.com/MedinaAlex/Lumiplan/tree/master/appV2).

Elle permet de créer un nouveau document à partir d'un document source généré par squash et d'un template créé par l'utilisateur
selon quelques règles (cf [README](https://github.com/MedinaAlex/Lumiplan/blob/master/appV2/README.md))

Une ihm est présente pour guider l'utilisateur, une fois le fichier source séléctionné, un arbre représentant les éléments généraux de chaque fiche de test
ainsi que les fiches elles-même sont représentant en tant qu'élément cochable. Ces éléments, s'ils sont décochés, ne seront pas présent dans le document final.

### Le serveur

Les éléments pour mettre corectement à jour Squash sont présent [ici](https://github.com/MedinaAlex/Lumiplan/blob/master/heimdall).
