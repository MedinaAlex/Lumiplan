#!/usr/bin/env python2.7
# coding: utf8
from zipfile import ZipFile


def extract(zip):
    """Extrait le fichier '/word/document.xml'
    d'une archive word dans le répertoire courant
    """

    myzip = ZipFile(zip, 'a')
    myzip.extract('word/document.xml', './../')
