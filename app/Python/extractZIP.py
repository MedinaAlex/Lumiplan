#!/usr/bin/env python2.7
# coding: utf8
from zipfile import ZipFile
import os


def extract(zip):
    """Extrait le fichier '/word/document.xml'
    d'une archive word dans le répertoire courant
    """

    myzip = ZipFile(zip, 'a')
    myzip.extract('word/document.xml', './../')


def extractAll(zip):
    """
    Extrait tout les fichiers d'une archive word dans un répertoire temporaire.
    """

    myzip = ZipFile(zip, 'a')
    myzip.extractall('./../tmp/')


def addFile(fileName):
    myzip = ZipFile('./../wordOut/' + fileName + '.zip', 'w')
    for file in os.listdir('./../tmp/word/'):
        myzip.write('./../tmp/word/' + file, file)
    myzip.close()
