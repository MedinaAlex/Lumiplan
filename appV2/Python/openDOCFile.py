# coding: utf8

from docx import Document
from collections import OrderedDict
import sys

import writeOnTemplate as wrt


def run(fileName):
    reload(sys)
    sys.setdefaultencoding("utf-8")

    document = Document(fileName)  # Document word

    para = document.paragraphs  # Liste des paragraphes du document
    tables = document.tables  # Liste des tables du document
    tt = iter(tables)  # itérateur des tables
    d2 = {}  # Liste de Dictionnaire ordonné contenant le contenu
    d = d2['Fiches'] = []
    dico = OrderedDict()
    pre, tag = [''] * 2
    element = ('Modifié', 'ID', 'Nature', 'Type', 'Statut',
               'Importance', 'Jalons',
               'ID:', 'Type:', 'Importance:', 'Jalons:')
    replacements = {'é': 'e', 'è': 'e', ':': ''}

    for elem in para:
        # Créé est le premier élément d'une fiche de test
        if 'Créé' in elem.text:
            # tag = ' '.join(pre.split()[:2])
            if dico:
                d.append(dico)

            dico = OrderedDict()

            tmp = elem.text.split(':')
            dico['Titre'] = pre
            dico['Cree'] = ':'.join(tmp[1:])
            dico['Etapes'] = []

        if 'Exigences' in elem.text.split():
            i = 1
            tmp = ''
            while 'Etape' not in para[para.index(elem) + i].text:
                tmp += '\t\t' + para[para.index(elem) + i].text + '\n'
                i += 1

            dico['Exigences'] = tmp

        if 'Description' in elem.text:
            i = 1
            while not para[para.index(elem) + i].text:
                i += 1

            dico['Description'] = para[para.index(elem) + i].text

            cell = tt.next()
            dico['Pre-requis'] = cell.row_cells(0)[1].text

        if 'Etape' in elem.text:
            etape = OrderedDict()
            num = ' '.join(elem.text.split()[1])
            etape['Numero'] = num

            for i in range(3):
                cell = tt.next()
                key = cell.row_cells(0)[0].text

                for src, dest in replacements.iteritems():
                    key = key.split()[0].replace(src, dest)

                etape[key] = cell.row_cells(0)[1].text

                if cell.row_cells(1) and i == 2:
                    key = cell.row_cells(1)[0].text

                    for src, dest in replacements.iteritems():
                        key = key.split()[0].replace(src, dest)

                    etape[key] = cell.row_cells(1)[1].text

            dico['Etapes'].append(etape)

        if any(str in element for str in(elem.text.split())):
            key = elem.text.split()[0]
            for src, dest in replacements.iteritems():
                key = key.split()[0].replace(src, dest)

            tmp = elem.text.split(':')
            dico[key] = ':'.join(tmp[1:])

        pre = elem.text
    d.append(dico)

    return d2


def activeDico(d2, l, template, name):
    active = []
    for j in l:
        if isinstance(j, tuple):
            active.append(' '.join(j))
        else:
            active.append(j)

    # crt.run(fileName, d)
    d2['general'] = []
    for act in active:
        if 'general' in act.split('.'):
            d2['general'].append(act.split('.')[1])

    for fiche in reversed(d2['Fiches']):
        index = d2['Fiches'].index(fiche)
        if fiche['Titre'] not in active:
            d2['Fiches'].pop(index)
            continue
        for key1, value1 in fiche.iteritems():
            if isinstance(value1, basestring) and 'Titre' not in key1:
                if fiche['Titre'] + '.' + key1 not in active:
                    d2['Fiches'][index].pop(key1)
            elif isinstance(value1, list):
                i = []
                for index2, elem in enumerate(value1):
                    if fiche['Titre'] + '.Etape' + elem['Numero'] not in active:
                        i.append(index2)
                        # d2['Fiches'][index][key1].pop(i)
                if i:
                    for suppr in reversed(i):
                        d2['Fiches'][index][key1].pop(suppr)
    d2['num'] = [i + 1 for i in range(len(d2['Fiches']))]


    wrt.run(d2, template, name)
    return (d2)

if __name__ == '__main__':
    run()
