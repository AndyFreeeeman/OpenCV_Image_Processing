#閾值分割-直方圖技術法

def caleGrayHist(image):
    #灰度影象的高、寬
    rows, cols = image.shape
    #儲存灰度直方圖
    grayHist = np.zeros([256], np.uint64) #影象的灰度級範圍是0~255      
    for r in range(rows):
        
        for c in range(cols):
            
            grayHist[image[r][c]] += 1
            
    return grayHist

def threshTwoPeaks(image):
    
    #計算灰度直方圖
    histogram = caleGrayHist(image)
    
    #找到灰度直方圖的最大峰值對應得灰度值
    maxLoc = np.where(histogram==np.max(histogram))
    firstPeak = maxLoc[0][0] #取第一個最大的灰度值
    
    #尋找灰度直方圖的第二個峰值對應得灰度值
    measureDists = np.zeros([256], np.float32)
    for k in range(256):
        measureDists[k] = pow(k-firstPeak,2)*histogram[k]
    maxLoc2 = np.where(measureDists==np.max(measureDists))
    secondPeak = maxLoc2[0][0]
    
    #找到兩個峰值之間的最小值對應的灰度值，作為閾值
    thresh = 0
    if firstPeak > secondPeak: #第一個峰值在第二個峰值右側
        temp = histogram[int(secondPeak):int(firstPeak)]
        minLoc = np.where(temp==np.min(temp))
        thresh = secondPeak + minLoc[0][0] + 1 #有多個波谷取左側的波谷
    else:
        temp = histogram[int(firstPeak):int(secondPeak)]
        minLoc = np.where(temp==np.min(temp))
        thresh = firstPeak + minLoc[0][0] + 1
        
    #找到閾值後進行閾值處理，得到二值圖
    threshImage_out = image.copy()
    threshImage_out[threshImage_out > thresh] = 255
    threshImage_out[threshImage_out <= thresh] = 0
    
    return (thresh, threshImage_out)

#THRESH_TRIANGLE與直方圖技術法類似(效果更好)

img = cv2.imread(r'wallpaper.jpg', cv2.IMREAD_GRAYSCALE)
the, dst = threshTwoPeaks(img)
the1 = 0
maxval = 255 
the1, dst1 = cv2.threshold(img, the1, maxval, cv2.THRESH_TRIANGLE + cv2.THRESH_BINARY)
print('The thresh is :', the)
print('The thresh1 is :', the1)
cv2.imshow("image", img)
cv2.imshow('thresh_out', dst)
cv2.imshow('thresh_out1', dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()   
