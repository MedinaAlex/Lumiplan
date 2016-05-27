"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from Tkinter import *
from tkFileDialog import *
import openDOCFile as op
import createTree as tr


def Ouvrir():
    f = open('./../arbre.txt', 'w')
    if introduction.get():
        filename = askopenfilename(title="Ouvrir un document texte",
                                   filetypes=[('txt file', '.txt'),
                                              ('all files', '.*')]
                                   )
        print(filename)

        file = open(filename)
        texte = file.read()
        file.close()
        f.write('Introduction : \n\t' + texte + '\n')
    f.close()
    dico, tagList = op.run()
    tr.run(dico, tagList)

# Main window
Mafenetre = Tk()
Mafenetre.title("Titre")

# Création d'un widget Menu
menubar = Menu(Mafenetre)

menufichier = Menu(menubar, tearoff=0)
menufichier.add_command(label="Ouvrir un document texte", command=Ouvrir)
menufichier.add_command(label="Quitter", command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

# Affichage du menu
Mafenetre.config(menu=menubar)

# Création d'un widget Canvas
Label1 = Label(Mafenetre, text='')
Label1.pack()

# Création d'un widget Checkbutton
introduction = IntVar()
introduction.set(1)  # ON
Checkbutton(Mafenetre, text="Introduction", variable=introduction).pack(
    padx=10, pady=10)

Description = IntVar()
Description.set(1)  # ON
Checkbutton(Mafenetre, text="Description", variable=Description)

exigence = IntVar()
Checkbutton(Mafenetre, text="Exigence", variable=exigence).pack(
    padx=10, pady=10)

CreeLe = IntVar()
Checkbutton(Mafenetre, text="Cree le", variable=CreeLe).pack(
    padx=10, pady=10)

ModifieLe = IntVar()
Checkbutton(Mafenetre, text="Modifie le", variable=ModifieLe).pack(
    padx=10, pady=10)

ID = IntVar()
Checkbutton(Mafenetre, text="ID", variable=ID).pack(
    padx=10, pady=10)

Nature = IntVar()
Checkbutton(Mafenetre, text="Nature", variable=Nature).pack(
    padx=10, pady=10)

Type = IntVar()
Checkbutton(Mafenetre, text="Type", variable=Type).pack(
    padx=10, pady=10)

Statut = IntVar()
Checkbutton(Mafenetre, text="Statut", variable=Statut).pack(
    padx=10, pady=10)

Importance = IntVar()
Checkbutton(Mafenetre, text="Importance", variable=Importance).pack(
    padx=10, pady=10)

Jalons = IntVar()
Checkbutton(Mafenetre, text="Jalons", variable=Jalons).pack(
    padx=10, pady=10)


PreRequis = IntVar()
Checkbutton(Mafenetre, text="Pré-requis", variable=PreRequis).pack(
    padx=10, pady=10)


Button(Mafenetre, text='Go', command=Ouvrir).pack(
    padx=5, pady=5)


# Utilisation d'un dictionnaire pour conserver une référence

Mafenetre.mainloop()
