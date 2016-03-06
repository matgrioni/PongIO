#!/usr/bin/python

import gopro
import time
import cv2 as cv

g = gopro.GoPro()
g.shutter()

time.sleep(3)
filename = g.getLastImage()

cv.namedWindow('Image frame', cv.WINDOW_NORMAL)
cv.resizeWindow('Image frame', 816, 612)
img = cv.imread('images/' + filename, 0)
template = cv.imread('template/template.jpg', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img, top_left, bottom_right, 255, 2)
print(top_left)

cv.imshow('Image frame', img)
cv.waitKey(0)
cv.destroyAllWindows()
