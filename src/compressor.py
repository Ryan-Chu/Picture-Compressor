from PIL import Image
import numpy as np

# Changes Pillow object to Numpy array
# Input: Pillow object
# Output: Numpy array
def ImagetoMatrix(picture):
    img = Image.open(picture)
    img_array = np.array(picture)
    return img_array

# Converts matrix to image then saves to output file
# Input: Matrix of image, desired output file name
# Output: Output file with image, returns nothing
def MatrixtoImage(revisedMatrix, outputpath):
    img = Image.fromarray(revisedMatrix)
    img.save(outputpath)
    return None