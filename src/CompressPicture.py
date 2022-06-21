from conversion import *
import os, sys
from PIL import Image
from pathlib import PurePath
from conversion import *
from compressor import *

# Find path for matrix
currentpath = os.getcwd()
imagepath = PurePath(currentpath).parent.joinpath(sys.argv[1])
outputpath = PurePath(currentpath).parent.joinpath(sys.argv[2])

# Check for any errors
checkArgtype(len(sys.argv) < 4,"Too many arguments.")
checkArgtype(os.path.exists(imagepath) == False, "Image doesn't exist.")
checkArgtype(os.path.exists(outputpath) == True, "File already exists, either delete file or run o as last input/argument.")
checkArgtype(len(sys.argv) > 3,"Too little arguments need to include out file or image name.")
checkArgtype(str.isdigit(sys.argv[3]),"Last input/argument needs to be number of singular values.")

# Converts it to numpy matrix, optimizes matrix, and converts back to image
currentImagematrix = ImagetoMatrix(imagepath)
optimized = convertMatrix(currentImagematrix, sys.argv[2])
MatrixtoImage(optimized, sys.argv[2])

print ("Image Conversion: Success!")

# Method to check if argument type is correct
# Input: Condition to check, string explaining desired value
# Output: Ends program by raising exception
def checkArgtype(condition, wantedType):
    if not (condition):
        raise Exception(wantedType)
    return

