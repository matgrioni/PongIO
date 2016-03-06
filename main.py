#!/usr/bin/python

import gopro
import time
import cv2 as cv

# from matplotlib import pyplot as plt


g = gopro.GoPro()
g.shutter()

time.sleep(3)
filename = g.getLastImage()

cv.namedWindow('Image frame', cv.WINDOW_NORMAL)
cv.resizeWindow('Image frame', 816, 612)
img = cv.imread('images/' + filename, 0)
template = cv.imread('template/template.jpg', 0)
w, h = template.shape[::-1]

functions = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for function in functions:
    method = eval(function)

    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(img, top_left, bottom_right, 255, 2)
    #plt.subplot(121),plt.imshow(res,cmap = 'gray')
    #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(img,cmap = 'gray')
    #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #plt.suptitle(meth)

    #plt.show()

cv.imshow('Image frame', img)
cv.waitKey(0)
cv.destroyAllWindows()
