# coding: utf8

from docx import Document
import json
import collections


def run():
    f = open('./../paraT.txt', 'w')
    a = open('./../arbre.txt', 'a')
    dd = open('./../dico.txt', 'w')

    document = Document('./../word/forTest.docx')  # Document word

    para = document.paragraphs  # Liste des paragraphes du document
    tables = document.tables  # Liste des tables du document
    tt = iter(tables)  # itérateur des tables

    d = collections.OrderedDict()  # Dictionnaire ordonné contenant le contenu
    pre = ''
    tagList = collections.OrderedDict()
    tag = ''
    element = ('Modifi', 'ID', 'Nature', 'Type', 'Statut',
               'Importance', 'Jalons',
               'ID:', 'Type:', 'Importance:', 'Jalons:')

    for elem in para:
        print('-' *60)
        print(elem.text.encode('utf-8'))
        if 'Exigence' in elem.text:  # On va écrire les prérequis avant
            cell = tt.next()

            d[tag].update({cell.row_cells(0)[0].text.encode('utf-8'):
                           cell.row_cells(0)[1].text.encode('utf-8')})
            f.write(cell.row_cells(0)[0].text.encode('utf-8') + '\n')
            f.write('\t' + cell.row_cells(0)[1].text.encode('utf-8'))

        f.write(elem.text.encode('utf-8') + '\n')

        if 'Créé' in elem.text.encode('utf8'):
            tag = ' '.join(pre.split()[:2])
            d[tag] = collections.OrderedDict()
            tagList[tag] = collections.OrderedDict()

        if ('Description' or 'Exigences') in elem.text.encode('utf8'):
            i = 1
            while not para[para.index(elem) + i].text:
                i += 1
            print('element = ' + elem.text)
            d[tag].update({elem.text.encode('utf-8'):
                           para[para.index(elem) + i].text})

        if 'Etape' in elem.text:
            etape = ' '.join(elem.text.split()[:2])

            if not tagList[tag]:
                tagList[tag] = {etape}
            else:
                tagList[tag].update({etape})

            d[tag][etape] = {}

            for _ in range(3):
                cell = tt.next()

                d[tag][etape].update({
                    cell.row_cells(0)[0].text.encode('utf-8'):
                    cell.row_cells(0)[1].text.encode('utf-8')})

                f.write(cell.row_cells(0)[0].text.encode('utf-8') + '\n')
                f.write('\t' + cell.row_cells(0)[1].text.encode(
                    'utf-8') + '\n')

        if any(str in element for str in(elem.text.split())):

            if not d[tag]:
                tmp = elem.text.split(':')
                d[tag] = collections.OrderedDict({tmp[0]: tmp[1]})
            else:
                tmp = elem.text.split(':')
                d[tag].update({tmp[0]: tmp[1]})

        pre = elem.text

    json.dump(d, dd)
    dd.close()

    for elem in d:
        a.write(elem + '\n')
        for tt in d[elem]:
            a.write('\t' + tt + '\n')
            if isinstance(d[elem][tt], basestring):
                a.write('\t\t' + d[elem][tt].encode('utf-8') + '\n')
            else:
                for dict in d[elem][tt]:
                    a.write('\t\t' + dict + '\n')
            # a.write('\t\t\t' + d[elem][tt][ccbb] + '\n')
    a.close()
    dd.close()
    f.close()
    print('done')
    return (d, tagList)
