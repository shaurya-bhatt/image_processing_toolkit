import numpy as np

def blur_image(img):
    kernel=np.ones((3,3))/9
    h,w=img.shape
    result=np.zeros((h-2,w-2))

    for i in range(h-2):
        for j in range(w-2):

            region=img[i:i+3,j:j+3]

            result[i,j]=np.sum(region*kernel)

    return result