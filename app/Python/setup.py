# setup.py
from distutils.core import setup
import py2exe
setup(console=["runAll.py", "changeExt.py", "XML.py", "extractZIP.py"])