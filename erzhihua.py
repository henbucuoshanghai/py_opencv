import cv2
import numpy as np

img = cv2.imread('dushushao.jpg',1) 
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,binary = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)    
#ret,binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)    #此处可控制黑白图哪个是底
#ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)   
#ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO) 
#ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)    


#binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 4)#自适应阈值 一个图不同区域不同阈值
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)   #OTSU很出名 |变成+也可以  binary可以直接显示保存
print(binary.shape) 
cv2.imwrite("binary.jpg",binary)
