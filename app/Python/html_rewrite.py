import os
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
    files = os.listdir('./../tmp/word')
    i = 0
    liste = ['<w:t>' + str(i) + '.</w:t>' for i in range(1, 201)] +
            ['NTRODUCTION', 'Moyenne']

    with open('./../tmp/word/document.xml') as f:
        for row in f:
            if '<w:t>' in row:
                ligne = row.replace('\t', '')
                ligne = ligne.replace(' ', '')
                tag = ligne[5:-6]
                if tag in liste:
                    pass
