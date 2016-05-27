# -- coding: utf-8 --
import Tix
from Tkinter import *


class View(object):
    def __init__(self, root, dico):
        self.root = root
        b_quitter = Button(self.root, text="Quitter", command=self.quitter)
        b_quitter.pack()
        self.makeCheckList(dico)

    def quitter(self):
        self.list = self.cl.getselection()
        self.root.destroy()
        self.root.quit()

    def makeCheckList(self, dico):
        self.replacements = {'Cree': 'Créé le', 'Modifie': 'Modifié le'}
        self.dico = dico
        self.element = ('ID', 'Description', 'Cree', 'Modifie',
                        'Nature', 'Type', 'Statut', 'Importance', 'Jalons',
                        'Pre-requis', 'Exigences')

        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack(fill=BOTH, expand=1)
        self.cl.hlist.add('general', text='general')

        for elem in self.element:
            self.cl.hlist.add('general.' + elem, text=replace_all(elem, self.replacements))
            self.cl.setstatus('general.' + elem, "off")

        self.cl.setstatus('general.ID', "on")
        self.cl.setstatus('general.Description', "on")

        for fiche in self.dico:
            self.cl.hlist.add(fiche['Titre'], text=fiche['Titre'])
            self.cl.setstatus(fiche['Titre'], "on")
            for element in fiche:
                if (isinstance(element, basestring) and
                    'Titre' not in element and
                    not isinstance(fiche[element], list)):

                    self.cl.hlist.add(fiche['Titre'] + '.' + element, text=replace_all(element, self.replacements))
                    self.cl.setstatus(fiche['Titre'] + '.' + element, self.cl.getstatus('general.' + element))

            for etape in fiche['Etapes']:
                self.cl.hlist.add(fiche['Titre'] + '.Etape' + etape['Numero'], text='Etape ' + etape['Numero'])
                self.cl.setstatus(fiche['Titre'] + '.Etape' + etape['Numero'], 'on')
        self.cl.autosetmode()

    def selectItem(self, item):
        if 'general' in item:
            for fiche in self.dico:
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
                    self.cl.setstatus(child, self.cl.getstatus('general.' + child.split('.')[1]))
                else:
                    self.cl.setstatus(child, stat)



def main(dico):
    root = Tix.Tk()
    root.geometry("400x800")
    view = View(root, dico)
    root.update()
    root.mainloop()
    return view.list

# if __name__ == '__main__':
#     main()


def replace_all(text, dict):
    for src, dest in dict.iteritems():
        text = text.replace(src, dest)
    return text
