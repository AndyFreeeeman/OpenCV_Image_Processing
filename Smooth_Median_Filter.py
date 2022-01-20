#影像平滑-中值濾波
#理論效果最好的平滑 / 保持邊緣、細節的區域性平滑演算法

#讀取圖片
img = cv2.imread('wallpaper.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#高斯濾波
#後數字調整模糊程度，1為原圖，往上增加，最高不超過15
result = cv2.medianBlur(img, 15)

#顯示影象
cv2.imshow("source img", img)
cv2.imshow("medianBlur", result)

#等待顯示
cv2.waitKey(0)
cv2.destroyAllWindows()
