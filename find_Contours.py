import cv2
import numpy as np
#这块代码有问题   但是命令就是这几句而已  四五句
img = cv2.imread('dushushao.jpg') 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 使用Otsu自动阈值，注意用的是cv2.THRESH_BINARY_INV
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找轮廓
_,contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)
area = cv2.contourArea(cnt)   #轮廓面积
perimeter = cv2.arcLength(cnt, True)#轮廓边长
x, y, w, h = cv2.boundingRect(cnt)  # 外接矩形
rect = cv2.minAreaRect(cnt)  # 最小外接矩形
x, y), radius = cv2.minEnclosingCircle(cnt)#最小外接圆
ellipse = cv2.fitEllipse(cnt)    #外界椭圆 
cv2.imwrite("resout.jpg",img)

#模板匹配    6种匹配方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
res = cv2.matchTemplate(img, template, method)  #前二个元素是直接读取的图片灰度图
#就一句话  简单的很
