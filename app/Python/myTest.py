# -*- coding: utf-8 -*-
'''
Created : 2015-03-12
@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate, RichText


def run(dico):

    tpl = DocxTemplate('./../test.docx')

    for fiche in dico['Fiches']:
        for key1, value1 in fiche.iteritems():
            if isinstance(value1, basestring):
                # fiche[key1] = RichText(value1)
                pass
            elif isinstance(value1, list):
                for elem in value1:
                    for key2, value2 in elem.iteritems():
                        elem[key2] = RichText(value2)
     

    context = dico

    tpl.render(context)
    tpl.save('./../mytest.docx')
