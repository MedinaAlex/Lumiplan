#!/usr/bin/env python2.7
# coding: utf8
from shutil import copy


def changeExt(file):
    """Change l'extension d'un fichier .docx pour du
    .zip en gardant le fichier original
    Le dossier de l'archive est 'zip'
    """

    copy('./../word/'+file+'.docx', './../zip/'+file+'.zip')
