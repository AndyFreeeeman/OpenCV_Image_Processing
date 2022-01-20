#影像平滑-高斯濾波
#保持邊緣、細節的區域性平滑演算法

#讀取圖片
img = cv2.imread('wallpaper.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#高斯濾波
#後二數字調整模糊程度，1為原圖，往上增加，最高不超過15
result = cv2.GaussianBlur(source, (15,15), 0)

#顯示圖形
titles = ['Source Image', 'GaussianBlur Image']  
images = [source, result]  
for i in range(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  
