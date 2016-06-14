#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
import re
import os
from lxml import etree


def xml(file, fileName):
    """Fonction qui met en forme le fichier xml et
    le déplace dans le dossier ./../xml/
    en le renommant selon son nom exact suivi de '_document',
    puis appelle la fonction 'test(file, fileName)'.
    """

    #  Fermeture automatique à la fin du traitement.
    with open("./../xml/" + fileName + "_document.xml", 'w') as f:
        #  Créer l'arbre xml et l'écrit dans le fichier
        f.write(etree.tostring(etree.parse(open(file)), pretty_print=True))

    print('construct xml tree done')

    os.remove(file)  # Supprime document.xml du dossier word

    # contenu("./../xml/" + fileName + "_document.xml", fileName)
    test("./../xml/" + fileName + "_document.xml", fileName)


def contenu(file, fileName):
    """Fonction appelée par la fonction xml(file, fileName)
    Fonction qui pour un fichier donné, va écrire dans un nouveau fichier,
    les lignes correspondant au texte écrit dans le fichier word.
    """

    fichier2 = open("./../xml/" + fileName + "_contenu.xml", 'w')

    with open(file) as f:  # Fermeture automatique à la fin du traitement
        for row in f:  # Pour chaque ligne du fichier
            #  Si c'est une ligne contenant du texte écrit dans le fichier word
            if re.search('((\w+|).*)</w:t>', row):
                fichier2.write(row)

    fichier2.close()  # Fermeture du fichier
    print('contenu done')


def all(file, fileName):
    buff = ''
    preRow = ''
    inP = False  # Variable pour savoir si l'on est dans un paragraphe

    fichier = open("./../xml/" + fileName + "_documentWithoutSpace.xml", 'w')

    with open(file) as f:
        for row in f:
            line = False
            preRow = row

            if(re.search("<w:p( .*|)>", row) and not
               re.search("<w:p( .*|)/>", row)):
                inP = True
            elif '</w:p>' in row:
                buff = ''
                if inP:
                    inP = False
                    continue

            if inP:
                if '<w:r>' in preRow and '<w:rPr>' not in row:
                    buff += preRow
                    buff += preRow[:-6] + '\t<w:rPr>\n'
                    buff += preRow[:-6] + '\t\t<w:rFonts w:cs="Arial"/>\n'
                    buff += preRow[:-6] + '\t\t<w:sz w:val="20"/>\n'
                    buff += preRow[:-6] + '\t</w:rPr>\n'
                    continue

                buff += row

                if(
                    any(str in row for str in('</w:t>',
                                              '<w:br w:type="page"/>',
                                              'Sommaire', 'DosSiteWeb',)
                        )  # and
                    # '> </w:t>' not in row
                ):
                    # On écrit ce que contient le buffer
                    fichier.write(buff)
                    buff = ''
                    inP = False
                    line = True

            if not inP and not line:
                # On écrit les lignes jusqu'au prochain paragraphe
                fichier.write(row)

    fichier.close()


def changeSize(file, fileName):
    preRow = ''
    buff = ''
    inP = False  # Variable pour savoir si l'on est dans un paragraphe

    fichier = open("./../xml/" + fileName + "_documentWithoutSpace.xml", 'w')

    with open(file) as f:
        for row in f:

            if(re.search("<w:p( .*|)>", row) and not
               re.search("<w:p( .*|)/>", row)):
                inP = True

            elif '</w:p>' in row:
                fichier.write(buff)
                buff = ''
                if inP:
                    inP = False
                    continue

            if inP:
                if '<w:r>' in preRow and '<w:rPr>' not in row:
                    buff += preRow
                    buff += preRow[:-6] + '\t<w:rPr>\n'
                    buff += preRow[:-6] + '\t\t<w:rFonts w:cs="Arial"/>\n'
                    buff += preRow[:-6] + '\t\t<w:sz w:val="20"/>\n'
                    buff += preRow[:-6] + '\t</w:rPr>\n'
                    continue
                buff += row

            if not inP:
                fichier.write(row)

    fichier.close()


def removeSpace(file, fileName):
    buff = ''
    inP = False  # Variable pour savoir si l'on est dans un paragraphe

    fichier = open("./../xml/" + fileName + "_documentWithoutSpace.xml", 'w')

    with open(file) as f:
        for row in f:
            line = False

            if(re.search("<w:p( .*|)>", row) and not
               re.search("<w:p( .*|)/>", row)):
                inP = True
            elif '</w:p>' in row:
                buff = ''
                if inP:
                    inP = False
                    continue

            if inP:
                buff += row

                if(
                    any(str in row for str in('</w:t>',
                                              '<w:br w:type="page"/>',
                                              'Sommaire', 'DosSiteWeb',)
                        )
                ):
                    # On écrit ce que contient le buffer
                    fichier.write(buff)
                    buff = ''
                    inP = False
                    line = True

            if not inP and not line:
                # On écrit les lignes jusqu'au prochain paragraphe
                fichier.write(row)

    fichier.close()


def test(file, fileName):
    buff = ''
    preRow = ''
    inP = False  # Variable pour savoir si l'on est dans un paragraphe
    other = False
    sdt = False
    fichier = open("./../xml/" + fileName + "_documentWithoutSpace.xml", 'w')

    with open(file) as f:
        for row in f:
            preRow = row

            # if 'TOC \\o "1-2" \\h \\z \\u' in row:
                #  continue

            if(re.search("<w:p( .*|)>", row) and not
               re.search("<w:p( .*|)/>", row)) and not sdt:
                inP = True
            elif '</w:p>' in row:
                inP = False
                if other:
                    fichier.write(buff + row)
                    buff = ''
                    other = False
                    continue
                if sdt:
                    fichier.write(row)
                buff = ''
                continue
            elif '<w:sdt>' in row:
                sdt = True
            elif '</w:sdt>' in row:
                sdt = False

            if inP:
                if '<w:r>' in preRow and '<w:rPr>' not in row:
                    buff += preRow
                    buff += preRow[:-6] + '\t<w:rPr>\n'
                    buff += preRow[:-6] + '\t\t<w:rFonts w:ascii="Arial" \
w:hAnsi="Arial" w:cs="Arial"/>\n'
                    buff += preRow[:-6] + '\t\t<w:sz w:val="20"/>\n'
                    buff += preRow[:-6] + '\t</w:rPr>\n'
                    continue

                buff += row

                if(
                    any(str in row for str in('</w:t>',
                                              '<w:br w:type="page"/>',
                                              'Sommaire', 'DosSiteWeb',
                                              '<w:pict>')
                        )
                ):
                    other = True

            if not inP:
                # On écrit les lignes jusqu'au prochain paragraphe
                fichier.write(row)

    fichier.close()
