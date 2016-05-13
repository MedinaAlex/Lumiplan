# coding: utf8
import changeExt as ext
import XML as xml
import extractZIP as zip
# import html_rewrite as html

import os
from shutil import rmtree


def run():
    dossiers = os.listdir('./../')

    if 'zip' not in dossiers:
        os.mkdir('./../zip')
    if 'xml' not in dossiers:
        os.mkdir('./../xml')
    if 'wordOut' not in dossiers:
        os.mkdir('./../wordOut')

    # Fichier source à modifier à choisir.
    file = raw_input("entrer le nom du fichier word sans l'extension :\n>>>")
    # Changement de l'extension du fichier pour une archive.
    ext.changeExt(file, 'docx', 'zip', './../word/', './../zip/')
    print('zipage done')

    # Extraction du fichier 'document.xml' de l'archive.
    zip.extract('./../zip/' + file + '.zip')
    print('extract done')

    # Mets en forme le document xml pour créer un arbre propre.
    xml.xml('./../word/document.xml', file)
    print('xml done')

    # Extrait tout les fichiers de l'archive pour modifier les fichiers html
    zip.extractAll('./../zip/' + file + '.zip')
    print('extractAll done')

    # Suppression des espaces des fichiers HTML
    # html.run()
    # print('rewrite html done')

    # zip.addFile(file)
    # print('create new zip done')

    # Création de la noouvelle archive et ajout des fichiers modifiés
    zip.zipdir('./../tmp', file)
    ext.changeExt(file, 'zip', 'docx', './../wordOut/', './../wordOut/')

    rmtree('./../zip')
    rmtree('./../xml')
    rmtree('./../tmp')
    os.remove('./../wordOut/' + file + '.zip')

if __name__ == '__main__':
    run()
