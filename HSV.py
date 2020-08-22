import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')
# BGR Values for the first 0,0 pixel
B, G, R = image[0, 0] 
print B, G, R
print image.shape
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print gray_img.shape
print gray_img[10, 50] 

