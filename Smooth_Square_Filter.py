#影像平滑-方框濾波

#讀取圖片
img = cv2.imread('wallpaper.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
#方框濾波
#後二數字調整模糊程度，1為原圖，往上增加
result = cv2.boxFilter(source, -1, (100,100), normalize=1)
 
#顯示圖形
titles = ['Source Image', 'BoxFilter Image']  
images = [source, result]  
for i in range(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show() 
