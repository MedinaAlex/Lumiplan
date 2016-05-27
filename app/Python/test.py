element = ('Cree le', 'Modifie le', 'ID', 'Nature', 'Type', 'Statut',
           'Importance', 'Jalons', 'Description', 'Pre-requis', 'Exigences couvertes')

for elem in element:
    print(elem + ' = IntVar()')
    print('Checkbutton(Mafenetre, text="' + elem + '", variable=' + elem + ').pack(\
side=LEFT, padx=10, pady=10)\n')
