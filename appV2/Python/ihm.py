# -- coding: utf-8 --
"""
Created : 2016-05-10
@author: Alex Medina
IHM d'utilisation
"""

import Tix
from Tkinter import *
from tkFileDialog import *

import openDOCFile as op


class View(object):
    """Classe de la vue"""

    def __init__(self, root):
        """Initialise la vue 'root'. Demande l'ouverture du fichier source.
        Puis créer l'arbre de contenu du fichier où chaque éléments est
        une checkBox qui va représenter les éléments souhaités.
        Créer aussi un bouton Ok.
        """

        # définit la vue
        self.root = root

        # Demande l'ouverture du fichier source
        fileName = askopenfilename(title="Ouvrir un fichier",
                                   filetypes=[
                                       ('docx files', '.docx'),
                                       ('all files', '.*')])

        # Récupère le dictionnaire du fichier
        self.dico = op.run(fileName)

        # Créer le bouton 'Ok' et l'affiche
        b_quitter = Button(self.root, text="Ok", command=self.quitter)
        b_quitter.pack()

        # Appele la méthode qui créer l'arbre de checkBox selon le dictionnaire
        self.makeCheckList()

    def quitter(self):
        """Méthode qui demande d'ouvrir un template et un fichier de destination
        Détruit la vue et quitte l'ihm en sauvegardant la liste des éléments
        séléctionnés
        """

        # Liste des éléments séléctionnés
        self.list = self.cl.getselection()

        self.template = askopenfilename(title="Ouvrir un template",
                                        filetypes=[
                                            ('docx files', '.docx'),
                                            ('all files', '.*')])

        self.name = asksaveasfile(mode='w', defaultextension='.docx').name
        self.root.destroy()
        self.root.quit()

    def makeCheckList(self):
        self.replacements = {'Cree': 'Créé le', 'Modifie': 'Modifié le'}
        self.element = ('ID', 'Description', 'Cree', 'Modifie',
                        'Nature', 'Type', 'Statut', 'Importance', 'Jalons',
                        'Pre-requis', 'Exigences')

        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack(fill=BOTH, expand=1)
        self.cl.hlist.add('general', text='general')

        for elem in self.element:
            self.cl.hlist.add('general.' + elem,
                              text=self.replace_all(elem, self.replacements))
            self.cl.setstatus('general.' + elem, "off")

        self.cl.setstatus('general.ID', "on")
        self.cl.setstatus('general.Description', "on")

        for fiche in self.dico['Fiches']:
            self.cl.hlist.add(fiche['Titre'], text=fiche['Titre'])
            self.cl.setstatus(fiche['Titre'], "on")
            for element in fiche:
                if (isinstance(element, basestring) and
                    'Titre' not in element and
                        not isinstance(fiche[element], list)):

                    self.cl.hlist.add(
                        fiche['Titre'] + '.' + element, text=self.replace_all(element, self.replacements))
                    self.cl.setstatus(
                        fiche['Titre'] + '.' + element, self.cl.getstatus('general.' + element))

            for etape in fiche['Etapes']:
                self.cl.hlist.add(
                    fiche['Titre'] + '.Etape' + etape['Numero'], text='Etape ' + etape['Numero'])
                self.cl.setstatus(
                    fiche['Titre'] + '.Etape' + etape['Numero'], 'on')
        self.cl.autosetmode()

    def selectItem(self, item):
        if 'general' in item:
            for fiche in self.dico['Fiches']:
                if self.cl.getstatus(fiche['Titre']) == 'on':
                    for eta in fiche:
                        if eta in self.element:
                            if (isinstance(eta, basestring) and
                                'Titre' not in eta and
                                    not isinstance(fiche[eta], list)):
                                self.cl.setstatus(fiche['Titre'] + '.' + eta,
                                                  self.cl.getstatus('general.' + eta))
        else:
            self.autoCheckChildren(item, self.cl.getstatus(item))

    def autoCheckChildren(self, item, stat):
        if self.cl.hlist.info_children(item):
            for child in self.cl.hlist.info_children(item):
                if child.split('.')[1] in self.element and stat == 'on':
                    self.cl.setstatus(child, self.cl.getstatus(
                        'general.' + child.split('.')[1]))
                else:
                    self.cl.setstatus(child, stat)

    def replace_all(self, text, dict):
        for src, dest in dict.iteritems():
            text = text.replace(src, dest)
        return text


def main():
    root = Tix.Tk()
    root.geometry("400x800")
    view = View(root)
    root.update()
    root.mainloop()
    dico = op.activeDico(view.dico, view.list, view.template, view.name)
    return(dico)

if __name__ == '__main__':
    main()
