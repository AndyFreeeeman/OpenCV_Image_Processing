#灰度直方圖-直方圖均衡化 Histogram Equalization

#缺點: 對處理的數據不加選擇(全局處理)，如此一來會增加背景雜訊的對比度並且降低有用訊號(特別亮或暗)的對比度


# read image
img = cv2.imread('wallpaper.jpg')

# 將圖片轉為灰階
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 圖形灰階均衡化
equalize_img = cv2.equalizeHist(gray_img)

# show image
cv2.imshow("image", gray_img)
cv2.imshow("equal_image", equalize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 畫圖
plt.hist(gray_img.ravel(), 256, [0, 255],label= 'original image')
plt.hist(equalize_img.ravel(), 256, [0, 255],label= 'equalize image')
plt.grid(color='gray', linestyle='dotted', linewidth=1)
plt.legend()
