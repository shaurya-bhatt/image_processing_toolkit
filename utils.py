from PIL import Image
import numpy as np


def load_image(path):
    img = Image.open(path)
    return np.array(img)


def save_image(array, path):
    img = Image.fromarray(array.astype('uint8'))
    img.save(path)