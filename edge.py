import numpy as np


def detect_edges(img):

    Kx = np.array([
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ])

    Ky = np.array([
        [-1,-2,-1],
        [0,0,0],
        [1,2,1]
    ])

    h, w = img.shape

    edges = np.zeros((h-2, w-2))

    for i in range(h-2):
        for j in range(w-2):

            region = img[i:i+3, j:j+3]

            gx = np.sum(region * Kx)
            gy = np.sum(region * Ky)

            edges[i,j] = np.sqrt(gx**2 + gy**2)

    return edges