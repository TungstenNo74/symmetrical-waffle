import cv2
import numpy as np
from viewer import view

class edge:
    HORIZONTAL = 0
    VERTICAL = 1


def findEdge(img, hvflag=0, threshhold=100):
    height, width, dunno = img.shape

    previous = 0
    current = 0
    iterator = 0

    for row in img:
        current = np.sum(row)
        if (current-previous > threshhold): break;
        previous = current
        iterator += 1

    print(iterator)
    return iterator

