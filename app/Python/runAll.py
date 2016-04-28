# coding: utf8
import changeExt as ext
import XML as xml
import extractZIP as zip


def run():
    file = raw_input("entrer le nom du fichier word sans l'extension : \n>>>")
    ext.changeExt(file)
    print('zipage done')

    zip.extract('./../zip/'+file+'.zip')
    print('extract done')

    xml.xml('./../word/document.xml', file)
    print('xml done')

if __name__ == '__main__':
    run()
