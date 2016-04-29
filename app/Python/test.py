import re
buff = ""
texte = False
with open("file") as f:
    for row in f:
        if re.search("<w:p(.*)", row):
            inP = True
        elif re.search("</w:p>"):
            inP = False

        if inP:
            buff += row
            if re.search("</w:t>", row):
                # On écrit ce que contient le buffer
                inP = False
                texte = True

        if not inP and texte:
            # On écrit les lignes jusqu'au prochain paragraphe
            True
