import cv2
import numpy as np

img1 = cv2.imread('1.png')
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 
ret,thres1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('binary 1', t1)

img2 = cv2.imread('2.png')
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) 
ret,thres2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('binary 2', t2)

img2=thres1-thres2
cv2.imshow('Missing elements',img2)
