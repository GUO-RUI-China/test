import cv2 as cv
import numpy as np

img=cv.imread("small_loli.jpg",1)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()