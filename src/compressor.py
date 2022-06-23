import numpy as np
from pathlib import Path
from matplotlib import image
from matplotlib import pyplot as plt

# Changes Pillow object to Numpy array
# Input: Pillow object
# Output: Numpy array
def ImagetoMatrix(picpath):
    inputmatrix = image.imread(picpath)[:,:,0]
    return inputmatrix

# Converts matrix to image then saves to output file
# Input: Matrix of image, desired output file name
# Output: Output file with image, returns nothing
def MatrixtoImage(revisedMatrix, outputPath):
    plt.figure()
    plt.imshow(revisedMatrix, cmap="gray")
    plt.savefig(outputPath)
    return None
