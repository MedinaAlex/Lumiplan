# -*- coding: utf-8 -*-
'''
Created : 2016-05-24
@author: Alex Medina
'''

from docxtpl import DocxTemplate, RichText


def run(dictionnaire, template, dst):
    """Fonction qui prend en paramètre, le dictionnaire de contenu du fichier
    source, un template '.docx' où va être écrit le contenu du dictionnaire
    et un chemin de destination où sera enregistré le fichier final.
    """

    tpl = DocxTemplate(template)

    for fiche in dictionnaire['Fiches']:
        for key1, value1 in fiche.iteritems():
            if isinstance(value1, basestring):
                # fiche[key1] = RichText(value1)
                pass
            elif isinstance(value1, list):
                for elem in value1:
                    for key2, value2 in elem.iteritems():
                        elem[key2] = RichText(value2)

    context = dictionnaire

    tpl.render(context)
    tpl.save(dst)
