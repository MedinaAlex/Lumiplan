# coding: utf8
import os
import re
from shutil import move


def run():
    for file in os.listdir('./../tmp/word'):
        if file.endswith('.html'):
            fichier = open('./../tmp/word/' + file + '.new', 'w')
            with open('./../tmp/word/' + file) as f:
                for row in f:
                    row = row.replace('&nbsp;', '')
                    fichier.write(row)
            fichier.close()
            move('./../tmp/word/' + file + '.new', './../tmp/word/' + file)


def arbre(fileName):
    """Création d'un arbre de contenu d'un fichier word"""

    titre = [str(i) + '.' for i in range(1, 201)]
    liste = ['ID:', 'Description']
    arbre = {}
    inTag = False
    inP = False
    preTexte =''

    with open('./../tmp/word/document.xml') as f:
        for row in f:
            if(re.search("<w:p( .*|)>", row) and not
               re.search("<w:p( .*|)/>", row)):
                inP = True
            elif '</w:p>' in row:
                inP = False
                texte =''
                preTexte =''

            elif '<w:t>' in row:
                ligne = row.replace('\t', '')
                ligne = ligne.replace(' ', '')
                ligne = ligne[5:-7]
                if ligne in titre:
                    tag = ligne
                    print(tag)
                    print(arbre)
                    inTag = True

            if inP and inTag:
                if '<w:t>' in row:
                    ligne = row.replace('\t', '')
                    ligne = ligne.replace(' ', '')
                    texte = ligne[5:-7]
                    if texte in liste:
                        print(texte)
                        preTexte = texte
                        print('tag =' + tag)
                        if tag in arbre:
                            arbre[tag].update({texte: None})
                        else:
                            print(arbre)
                            arbre[tag] = {texte: None}
    #                 else:
    #                     if tag in arbre:
    #                         arbre[tag].update({preTexte: texte})
    #                     else:
    #                         arbre[tag] = {preTexte: texte}
    print(arbre)
