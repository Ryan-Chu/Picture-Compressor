import numpy as np
# Error and exception handling under main

# Calculate non zero svd values
# Input: Matrix of an image, optional: desired number of singular values
# Output: New optimized matrix
def convertMatrix(workingMatrix, differentsvd = 0):
    u, s, v = np.linalg.svd(workingMatrix)
    i = len(workingMatrix)
    m, n= workingMatrix.shape
    Newpicture = np.zeros((m,n))
    if(differentsvd != 0):
        Newpicture = (u[:,:differentsvd]@np.diag(s[:differentsvd])@(v[:differentsvd,:]))
        return Newpicture
    else:
        Newpicture = (u[:,:i]@np.diag(s[:i])@(v[:i,:]))
        return Newpicture
