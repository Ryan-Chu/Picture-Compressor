#from compressor.py
from conversion import *
import os, sys
from pathlib import PurePath

currentpath = os.getcwd()
imagepath = PurePath(currentpath).parent.joinpath(sys.argv[1])
print(imagepath)