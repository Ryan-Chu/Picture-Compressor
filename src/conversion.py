import numpy as np
# Error and exception handling under main

# Calculate non zero svd values
# Input: Matrix of an image, optional: desired number of singular values
# Output: New optimized matrix
def convertMatrix(workingMatrix):
    u, s, v = np.linalg.svd(workingMatrix)
    i = len(s)
    m, n= workingMatrix.shape
    Newpicture = np.zeros((m,n))
    Newpicture = (u[:,:i])@np.diag(s[:i])@(v[:i,:])
    return Newpicture
