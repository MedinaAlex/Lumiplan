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
