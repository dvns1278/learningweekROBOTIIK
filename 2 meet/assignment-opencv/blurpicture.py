import cv2 as cv2
import numpy as np

img = cv2.imread('resource/sourceimage.png')
cv2.imshow('original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray scale', gray)

blur = cv2.blur(img,(5,5))
cv2.imshow('blur image', blur)

gauss = cv2.GaussianBlur(blur, (5,5), 0)
cv2.imshow('gauss image', gauss)

median = cv2.medianBlur(img, 5)
cv2.imshow('median image', median)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('bilateral image', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()