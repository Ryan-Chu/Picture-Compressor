from PIL import Image
import numpy as np

#This handles all conversions
def ImagetoMatrix(picture):
    img = Image.open(picture)
    img_array = np.array(picture)
    return img_array

def MatrixtoImage(revisedMatrix, outputpath):
    img = Image.fromarray(revisedMatrix)
    img.save(outputpath)
    return None