import os
import re
from shutil import move


def run():
    for file in os.listdir('./../tmp/word'):
        if file.endswith('.html'):
            fichier = open('./../tmp/word/' + file + '.new', 'w')
            with open('./../tmp/word/' + file, 'r') as f:
                for row in f:
                    if not row or re.search('<p>&nbsp;</p>', row):
                        continue
                    fichier.write(row)
            fichier.close()
            move('./../tmp/word/' + file + '.new', './../tmp/word/' + file)
