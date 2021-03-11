import cv2
import numpy as np

img = cv2.imread('dushushao.jpg',1) #1就是直接读原图，0则是单通道
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#读原图才能  
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)   #OTSU很出名  binary可以直接显示保存
print(binary.shape) #单通道 黑白图二值图
cv2.imwrite("binary.jpg",binary)   #对黑白图膨胀腐蚀
#定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(14,1)) #十字形#得到一个5x5的矩形cv2.MORPH_RECT #cv2.MORPH_ELLIPSE
iterations = 10   #执行开闭运算的次数
#膨胀腐蚀  可以是单通道 也可三通道 也可二值图 随便
'''
erode_res = cv2.erode(binary, kernel,iterations)
dilate_res = cv2.dilate(binary, kernel) #所有命令可以不用写迭代次数

cv2.imwrite('fushi.jpg',erode_res)
cv2.imwrite('dilate.jpg',dilate_res)
'''
'''
open_res= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations)
close_res = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations)

cv2.imwrite('open.jpg',open_res)
cv2.imwrite('close.jpg',close_res)
'''
'''
erode_res = cv2.erode(binary, kernel) #kernel是(1,2)则留下数字  (14,1)则留下横线  直接(30,1)
cv2.imwrite('tmp.jpg',erode_res)      #查看中间环节对不对  则方便修改kernel大小
dilate_res = cv2.dilate(erode_res, kernel)#腐蚀后的结果 膨胀回去  保留目标
cv2.imwrite('open.jpg',dilate_res)
'''
'''
openn = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel,iterations=1)# (14,1)OPEN换成TOPHAT  就是作差
cv2.imwrite('openn.jpg',openn)
'''
close = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)# CLOSE换成BLACKHAT  就是作差
cv2.imwrite('close.jpg',close)
