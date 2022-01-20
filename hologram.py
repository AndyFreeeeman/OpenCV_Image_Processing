#灰度直方圖-畫灰度直方圖

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
def calcGrayHist(I):
    # 計算灰度直方圖
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
            
    return grayHist
 
img = cv.imread('wallpaper.jpg', 0)

grayHist = calcGrayHist(img)

x = np.arange(256)

# 繪製灰度直方圖
plt.plot(x, grayHist, 'r', linewidth=2, c='blue')
plt.xlabel("Gray Label")
plt.ylabel("Number of pixels")
plt.title('Gray Hist Plot')
plt.grid(color='gray', linestyle='dotted', linewidth=1)

plt.show()
