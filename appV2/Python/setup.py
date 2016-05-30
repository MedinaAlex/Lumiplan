# setup.py
from distutils.core import setup
import py2exe
import glob
import sys
import os
import os.path

def listdirectory(path): 
    return filter(os.path.isfile, glob.glob(path + os.sep + '*')) 

data_files=[ 
          ('Dlls', glob.glob(sys.prefix+'/DLLs/tix8.4.3.dll')), 
          ('tcl/tix8.4.3', listdirectory(sys.prefix+'/tcl/tix8.4.3')), 
          ('tcl/tix8.4.3/bitmaps', listdirectory(sys.prefix+'/tcl/tix8.4.3/bitmaps')), 
          ('tcl/tix8.4.3/pref', listdirectory(sys.prefix+'/tcl/tix8.4.3/pref')), 
           ] 

setup(
	console=[{'script': 'ihm.py'}],
	options={
        'py2exe':
        {
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip', 'docx', 'docxtpl', 'Tix', 'Tkinter'],
        }
    },
    data_files = data_files
)
