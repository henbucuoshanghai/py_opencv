import cv2
import numpy as np
# 1.Canny边缘检测
img = cv2.imread('shaizi.jpg', 0)
edges = cv2.Canny(img, 30, 70)
cv2.imwrite('resout.jpg', np.hstack((img, edges)))

# 2.先阈值，后边缘检测
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)
cv2.imwrite('resout.jpg', np.hstack((img, edges)))
