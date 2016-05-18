"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from Tkinter import *
from tkFileDialog import *
import openDOCFile as op


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
    side=LEFT, padx=10, pady=10)

exigence = IntVar()
Checkbutton(Mafenetre, text="Exigence", variable=exigence).pack(
    side=LEFT, padx=10, pady=10)

Button(Mafenetre, text='Go', command=Ouvrir).pack(
    side=LEFT, padx=5, pady=5)


# Utilisation d'un dictionnaire pour conserver une référence

Mafenetre.mainloop()
