import cv2
import numpy as np
import edger

img = cv2.imread("testRef.jpg")

img = np.bitwise_not(img)

# Horizontal Test
firstRow = edger.findEdge(img)
firstColum = edger.findEdge(img,1)

img[firstRow]=[255,0,0]
img[:,firstColum]=[255,0,0]

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
