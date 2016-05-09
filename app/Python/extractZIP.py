#!/usr/bin/env python2.7
# coding: utf8
from zipfile import ZipFile, ZIP_DEFLATED
import os
from shutil import copy, rmtree, move
import tempfile


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
    copy('./../zip/' + fileName + '.zip', './../wordOut/' + fileName + '.zip')
    myzip = ZipFile('./../wordOut/' + fileName + '.zip', 'a')
    for file in os.listdir('./../tmp/word/'):
        myzip.write('./../tmp/word/' + file, 'word\\' + file, ZIP_DEFLATED)
    myzip.close()


def remove_from_zip(zip, *fileNames):
    tempdir = tempfile.mkdtemp()
    try:
        tempname = os.path.join(tempdir, 'new.zip')
        with ZipFile(zip, 'r') as zipread:
            with ZipFile(tempname, 'w') as zipwrite:
                for item in zipread.infolist():
                    if item.fileNames not in fileNames:
                        data = zipread.read(item.fileNames)
                        zipwrite.writestr(item, data)
        move(tempname, zip)
    finally:
        rmtree(tempdir)


def zipdir(path, fileName):
    move("./../xml/" + fileName + "_documentWithoutSpace.xml",
         './../tmp/word/document.xml')
    myzip = ZipFile('./../wordOut/' + fileName + '.zip', 'w')
    for root, dirs, files in os.walk(path):
        for file in files:
            myzip.write(os.path.join(root, file), root[9:] + '\\' + file,
                        ZIP_DEFLATED)
    myzip.close()
    rmtree('./../tmp')
