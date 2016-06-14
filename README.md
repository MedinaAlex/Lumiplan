# Présentation du stage
Le stage chez Lumiplan consiste à réaliser un outil de traitement plus ou moins automatique 
des documents word fournis par SquashTm, un gestionnaire de référentiel de test. En effet, 
les documents de sorties de SquashTm ont une mise en forme qui n'est pas adaptée pour 
une présentation aux clients de Lumiplan.

Je dois donc réaliser diverses opérations qui permettront d'avoir une mise en forme des documents convenable.

Je dois par ailleurs permettre aux utilisateurs de cet outil, de créer de nouveaux documents selon des templates
en sélectionnant des extraits depuis d'autres fichiers.

Il y a aussi du travail à réaliser sur un serveur où se trouve la base de données de SquashTm, je dois mettre à jour Squash ainsi que sa base de données.

Pour ne pas travailler directement sur le serveur, j'utilise une machine virtuelle Debian, sur laquelle j'ai récupéré la base de données du serveur.

Il peut y avoir des changements dans les objectifs de ce stage selon la complexité de résolution de celui-ci.

### L'application

L'application finale se trouve dans le dossier [appV2](https://github.com/MedinaAlex/Lumiplan/tree/master/appV2).z

Elle permet de créer un nouveau document à partir d'un document source généré par Squash et d'un template créé par l'utilisateur
selon quelques règles (cf [README](https://github.com/MedinaAlex/Lumiplan/blob/master/appV2/README.md)).

Une IHM (Interface Homme Machine) est présente pour guider l'utilisateur, une fois le fichier source séléctionné, un arbre représentant les éléments généraux de chaque fiche de test
ainsi que les fiches elles-mêmes sont représentés en tant qu'éléments cochables. Ces éléments, s'ils sont décochés, ne seront pas présent dans le document final.

### Le serveur

Les éléments pour mettre correctement à jour Squash sont présent [ici](https://github.com/MedinaAlex/Lumiplan/blob/master/heimdall).
