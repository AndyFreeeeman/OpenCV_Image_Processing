#閾值分割-熵演算法


def caleGrayHist(image):
    #灰度影象的高、寬
    rows, cols = image.shape
    #儲存灰度直方圖
    grayHist = np.zeros([256], np.uint64) #影象的灰度級範圍是0~255      
    for r in range(rows):
        for c in range(cols):
            
            grayHist[image[r][c]] +=1
            
    return grayHist

def threshEntropy(image):
    rows, cols = image.shape
    #求灰度直方圖
    grayHist = caleGrayHist(image)
    #歸一化灰度直方圖，即概率直方圖
    normGrayHist = grayHist/float(rows*cols)
    
    #第一步：計算累加直方圖，也成為零階累矩陣
    zeroCumuMoment = np.zeros([256], np.float32)
    for k in range(256):
        if k == 0 :
            zeroCumuMoment[k] = normGrayHist[k]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k-1] + normGrayHist[k]
    #第二步：計算各個灰度級的熵
    entropy = np.zeros([256], np.float32)
    for k in range(256):
        if k == 0 :
            if normGrayHist[k] == 0 :     
                entropy[k] = 0
            else:
                entropy[k] = - normGrayHist[k] * math.log10(normGrayHist[k])
        else:
            if normGrayHist[k] == 0 :
                entropy[k] = entropy[k-1]
            else:
                entropy[k] = entropy[k-1] - normGrayHist[k] * math.log10(normGrayHist[k])
    #第三步：找閾值
    fT = np.zeros([256], np.float32)
    ft1, ft2 = 0.0, 0.0
    totalEntropy = entropy[255]
    for k in range(255):
        #找最大值
        maxFront = np.max(normGrayHist[0:k+1])
        maxBack = np.max(normGrayHist[k+1:256])
        if maxFront==0 or zeroCumuMoment[k]==0 or maxFront==1 or zeroCumuMoment[k]==1 or totalEntropy==0 :
            ft1 = 0
        else:
            ft1 = entropy[k]/totalEntropy*(math.log10(zeroCumuMoment[k])/math.log10(maxFront))
        if maxBack==0 or 1-zeroCumuMoment[k]==0 or maxBack==1 or 1-zeroCumuMoment[k]==1 :
            ft2 = 0
        else:
            if totalEntropy == 0 :
                ft2 = (math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
            else:
                ft2 = (1-entropy[k]/totalEntropy)*(math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
        fT[k] = ft1 + ft2
    
    #找到最大值索引
    threshLoc = np.where(fT==np.max(fT))
    thresh = threshLoc[0][0]
    #閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    
    return (thresh, threshold)
    
img = cv2.imread(r'wallpaper.jpg', cv2.IMREAD_GRAYSCALE)
the, dst = threshEntropy(img)
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
