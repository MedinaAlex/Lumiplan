# -*- coding: utf-8 -*-
'''
Created : 2015-03-12
@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate, RichText

def run(dico):

	tpl = DocxTemplate('./../test.docx')


	context = dico

	tpl.render(context)
	tpl.save('./../mytest.docx')
