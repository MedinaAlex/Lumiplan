# coding: utf8
import changeExt as ext
import XML as xml
import extractZIP as zip
import html_rewrite as html


def run():
    file = raw_input("entrer le nom du fichier word sans l'extension :\n>>>")
    ext.changeExt(file, 'docx', 'zip', './../word/', './../zip/')
    print('zipage done')

    zip.extract('./../zip/' + file + '.zip')
    print('extract done')

    xml.xml('./../word/document.xml', file)
    print('xml done')

    zip.extractAll('./../zip/' + file + '.zip')
    print('extractAll done')

    # html.run()
    print('rewrite html done')

    # zip.addFile(file)
    # print('create new zip done')

    zip.zipdir('./../tmp', file)
    ext.changeExt(file, 'zip', 'docx', './../wordOut/', './../wordOut/')

if __name__ == '__main__':
    run()
