import re
i = 0
t = 0
inP = False
inT = False
tt = False
with open("./../tmp/word/document.xml") as f:
    for row in f:
        if tt and re.search("<w:p(| .*)>", row) and not re.search("<w:p(| .*)/>", row):
            i += 1

        if '<w:tbl>'in row:
            t += 1
            inT = True
        elif '</w:tbl>':
            inT = False

        if '<w:t>' in row:
            tt = True
print(i)
print(t)