from conversion import *
import os, sys
from PIL import Image
from pathlib import PurePath
from conversion import *
from compressor import *

# Method to check if argument type is correct
# Input: Condition to check, string explaining desired value
# Output: Ends program by raising exception
def checkArgtype(condition, wantedType):
    if (condition):
        raise Exception(wantedType)
    return

# Find path for matrix
currentpath = os.getcwd()
imagepath = PurePath(currentpath).parent.joinpath('Images').joinpath(sys.argv[1])
outputpath = PurePath(currentpath).parent.joinpath('Images').joinpath(sys.argv[2])

# Check for any errors
checkArgtype(len(sys.argv) != 3,"Wrong amount of arguments.")
checkArgtype(os.path.exists(imagepath) == False, "Image doesn't exist.")

# Converts it to numpy matrix, optimizes matrix, and converts back to image within output file
currentImagematrix = ImagetoMatrix(str(imagepath))
optimized = convertMatrix(currentImagematrix)
MatrixtoImage(optimized, sys.argv[2])

print ("Image Conversion: Success!")