from PIL import Image
import numpy as np
from pathlib import Path

# Changes Pillow object to Numpy array
# Input: Pillow object
# Output: Numpy array
def ImagetoMatrix(pic):
    img = Image.open(str(pic))
    img = img.convert("L")
    img_array = np.array(img)
    return img_array

# Converts matrix to image then saves to output file
# Input: Matrix of image, desired output file name
# Output: Output file with image, returns nothing
def MatrixtoImage(revisedMatrix, outputPath):
    img = Image.fromarray(revisedMatrix)
    img.convert('RGB').save(outputPath)
    return None