import cv2
import numpy as np
# coding=UTF-8
img = cv2.imread('dushushao.jpg',1) 
blur = cv2.blur(img, (3, 3))           # 1中值滤波
gas_blur = cv2.GaussianBlur(img, (3, 3),0)  #高斯滤波
median = cv2.medianBlur(img, 5)         #中值滤波
bi = cv2.bilateralFilter(img, 5, 75, 75)  # 双边滤波  效果最好最佳



res = np.hstack((img, blur, gau_blur))  #可以直观对比
'''
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
binary=cv2.filter2D(img, -1, kernel=kernel) #锐化
'''
cv2.imwrite("resout.jpg",bi)
