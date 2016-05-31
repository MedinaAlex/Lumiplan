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
        """Créer l'arbre de contenu façon checkList pour séléctionner les
        éléments voulu dans le document final.
        """
        # On va remplacer le texte pour un  meilleur affichage
        self.replacements = {'Cree': 'Créé le', 'Modifie': 'Modifié le'}

        # Liste d'éléments pour faciliter le code avec des boucles
        self.element = ('ID', 'Description', 'Cree', 'Modifie',
                        'Nature', 'Type', 'Statut', 'Importance', 'Jalons',
                        'Pre-requis', 'Exigences')

        # Définition de la checkList, la méthode 'selectIten' est appelée
        # lors d'un clic sur la checkList
        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack(fill=BOTH, expand=1)

        # Ajout d'un élément père 'general'
        self.cl.hlist.add('general', text='géneral')

        # On va ajouter les éléments de la liste au parent 'general'
        for elem in self.element:
            self.cl.hlist.add('general.' + elem,
                              text=self.replace_all(elem, self.replacements))
            # On les décoches de base
            self.cl.setstatus('general.' + elem, "off")

        # On coche les éléments suivant
        self.cl.setstatus('general.ID', "on")
        self.cl.setstatus('general.Description', "on")

        # On va ajouter les fiches ainsi que leurs éléments et étapes
        for fiche in self.dico['Fiches']:
            # On ajoute un élément père pour la fiche qu'on coche de base
            self.cl.hlist.add(fiche['Titre'], text=fiche['Titre'])
            self.cl.setstatus(fiche['Titre'], "on")

            # On va ajouter ses éléments
            for element in fiche:
                if (isinstance(element, basestring) and
                    'Titre' not in element and
                        not isinstance(fiche[element], list)):

                    # Ajoute les éléments à l'arbre
                    self.cl.hlist.add(
                        fiche['Titre'] + '.' + element,
                        text=self.replace_all(element, self.replacements))

                    # Définit le status de la case selon les éléments généraux
                    self.cl.setstatus(
                        fiche['Titre'] + '.' + element,
                        self.cl.getstatus('general.' + element))

            # On va ajouter les étapes de chaque fiches
            for etape in fiche['Etapes']:
                self.cl.hlist.add(
                    fiche['Titre'] + '.Etape' + etape['Numero'],
                    text='Etape ' + etape['Numero'])

                # On les coches de base
                self.cl.setstatus(
                    fiche['Titre'] + '.Etape' + etape['Numero'], 'on')

        # Permet de faire de tous les éléments, des cases cochables
        self.cl.autosetmode()

    def selectItem(self, item):
        """Méthode appelée lors d'un clic sur la checkList, Si l'élément coché
        à comme père 'général', on va mettre pour chaque fiches, le même status
        pour le même élément que l'élément coché. Sinon on appelle la méthode
        'autoCheckChildren'.
        """

        if 'general' in item:
            for fiche in self.dico['Fiches']:
                if self.cl.getstatus(fiche['Titre']) == 'on':
                    for eta in fiche:
                        if eta in self.element:
                            if (isinstance(eta, basestring) and
                                'Titre' not in eta and
                                    not isinstance(fiche[eta], list)):
                                self.cl.setstatus(fiche['Titre'] + '.' + eta,
                                                  self.cl.getstatus(
                                    'general.' + eta))
        else:
            self.autoCheckChildren(item, self.cl.getstatus(item))

    def autoCheckChildren(self, item, stat):
        """Méthode qui définit les enfants d'un élément par le même status
        sauf pour les éléments qui sont présent dans 'general' qui sont
        définis par leur status propre.
        Attention, pas de récursion, marche car il n'y a que 2 niveaux.
        """

        # L'item a des enfants
        if self.cl.hlist.info_children(item):
            # Pour chacun de ses enfants
            for child in self.cl.hlist.info_children(item):
                # Si c'est un élément de 'general'
                if child.split('.')[1] in self.element and stat == 'on':
                    self.cl.setstatus(child, self.cl.getstatus(
                        'general.' + child.split('.')[1]))
                else:
                    self.cl.setstatus(child, stat)

    def replace_all(self, text, dict):
        """Méthode qui remplace un string selon un dictionnaire"""

        for src, dest in dict.iteritems():
            text = text.replace(src, dest)
        return text


def main():
    """Méthode lancée au démarrage qui créer une vue et va appeler la méthode
    qui va créer le dictionnaire final.
    """
    # On créer une ihm
    root = Tix.Tk()
    # On définit sa taille
    root.geometry("400x800")
    # On créer la vue
    view = View(root)
    # On met à jour les paramètres de taille
    root.update()
    # On boucle sur l'ihm
    root.mainloop()
    # On appelle cette méthode lorque l'ihm est fermée
    dico = op.activeDico(view.dico, view.list, view.template, view.name)
    return(dico)


if __name__ == '__main__':
    main()
