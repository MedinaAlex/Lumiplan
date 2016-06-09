# Mettre à jour Squash
### Mettre à jour la base de données
Des scripts sont disponibles dans le dossier *database-scprits*

Avec une base Mysql, il faut lancer chaque script d'une version supérieur à votre version actuelle.
pour savoir la version de votre serveur Squash, sur le site de squash, dans administration, VERSION
Au 09 juin 2016, la version de Squash est 1.12.2, il faudra donc lancer les scripts:
- mysql-upgrade-to-1.12.3.sql
- mysql-upgrade-to-1.13.0.sql
- mysql-upgrade-to-1.13.1.sql

Pour exécuter un script:
```
# mysql -h HOST -u USER -p squashtm < /path/to/script.sql 
```



### Configuration de Squash
Le démon de la configuration actuelle de Squash sur le serveur heimdall est *squash-tm*.
Toutes les informations nécessaire à une réinstallation de Squash selon la configuration actuelle sont présentes dans ce fichier.

### Attention
Il y a certain changement de configuration entre la version 1.12 et 1.13
- Les plugins ne sont plus à installer dans le dossier *bundles* mais dans le dossier *plugins*
- Le fichier de configuration est *conf/squash.tm.cfg.properties*
- Squash est désormais déployé sur un serveur TomCat 7.([Installer Squash sur un serveur Tom Cat existant](https://sites.google.com/a/henix.fr/wiki-squash-tm/installation-and-exploitation-guide/2---installation-of-squash-tm/2-08-deploy-squash-tm-in-tomcat))
