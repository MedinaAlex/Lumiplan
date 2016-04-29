#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
import re
import os
from lxml import etree


def xml(file, fileName):
    """Fonction qui met en forme le fichier xml et
    le déplace dans le dossier ./../xml/
    en le renommant selon son nom exact suivi de '_document',
    puis appelle la fonction 'contenu(file, fileName)'.
    """

    #  Fermeture automatique à la fin du traitement.
    with open("./../xml/" + fileName + "_document.xml", 'w') as f:
        #  Créer l'arbre xml et l'écrit dans le fichier
        f.write(etree.tostring(etree.parse(open(file)), pretty_print=True))

    print('construct xml tree done')

    os.remove(file)  # Supprime document.xml du dossier word

    contenu("./../xml/" + fileName + "_document.xml", fileName)


def contenu(file, fileName):
    """Fonction appelée par la fonction xml(file, fileName)
    Fonction qui pour un fichier donné, va écrire dans un nouveau fichier,
    les lignes correspondant au texte écrit dans le fichier word.
    """

    fichier = open(file, 'r')
    fichier2 = open("./../xml/" + fileName + "_contenu.xml", 'w')

    with fichier:  # Fermeture automatique à la fin du traitement
        for row in fichier:  # Pour chaque ligne du fichier
            #  Si c'est une ligne contenant du texte écrit dans le fichier word
            if re.search('((\w+|).*)</w:t>', row):
                fichier2.write(row)

    fichier2.close()  # Fermeture du fichier
    print('regex done')
    removeSpace(file, fileName)


def removeSpace(file, fileName):
    buff = ""
    inP = False
    inT = False
    fichier = open("./../xml/" + fileName + "_documentWithoutSpace.xml", 'w')

    with open(file) as f:
        for row in f:
            line = False
            if re.search("<w:tbl>", row):
                inT = True
            elif re.search("</w:tbl>", row):
                inT = False

            if(re.search("<w:p( .*|)>", row) and not
               re.search("<w:p( .*|)/>", row)):
                inP = True
            elif re.search("</w:p>", row):
                buff = ""
                if inP and not inT:
                    inP = False
                    continue
                inP = False

            if inP and not inT:
                buff += row
                if(re.search("</w:t>", row)or
                   re.search('<w:br w:type="page"/>', row)):
                    # On écrit ce que contient le buffer
                    fichier.write(buff)
                    buff = ""
                    inP = False
                    line = True

            if inT or not inP and not line:
                # On écrit les lignes jusqu'au prochain paragraphe
                fichier.write(row)

    fichier.close()
