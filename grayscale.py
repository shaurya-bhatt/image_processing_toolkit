import numpy as np

def convert_to_grayscale(img):
    gray=np.dot(img[::3],[0.299, 0.587, 0.114])
    return gray