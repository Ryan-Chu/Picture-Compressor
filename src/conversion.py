import numpy as np
# Error and exception handling will be under main
# Test file coming soon

# Calculate non zero singular values
# Input: Matrix of singular values
# Output: Matrix of non zero singular values
def calculateImportant(svdMatrix):
    importance = 0
    for x in svdMatrix:
        importance += 1
    return importance

# Calculate non zero svd values
# Input: Matrix of an image, optional: desired number of singular values
# Output: New optimized matrix
def convertMatrix(workingMatrix, differentsvd = 0):
    u, s, v = np.linalg.svd(workingMatrix)
    i = calculateImportant(u)
    m, n = workingMatrix.shape
    Newpicture = np.zeros(m,n)
    if(differentsvd != 0):
        Newpicture[:,:] = s[differentsvd]*np.outer(u[:,differentsvd]),np.transpose(v[differentsvd,:])
        return Newpicture
    else:
        Newpicture[:,:] = s[i]*np.outer(u[:,i]),np.transpose(v[i,:])
        return Newpicture

