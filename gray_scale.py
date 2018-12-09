import cv2

image = cv2.imread('1.png')        # change the image name with your image name
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Original Image', image)
cv2.imshow('Gray Scale Image',gray)
