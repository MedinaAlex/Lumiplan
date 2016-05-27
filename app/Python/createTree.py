def run(dico, tagList):
    pre = ''
    with open('./../arbre.txt') as f:
        for row in f:
            nb = row.count('\t')
            if not nb:
                texte = 'element 1'
                elem = row
            elif nb == 1:
                texte = 'element 2'
            elif nb == 2:
                texte = 'contenu'


