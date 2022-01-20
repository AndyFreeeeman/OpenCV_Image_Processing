#灰度直方圖-自適應直方圖均衡化 Adaptive Histogram Equalization AHE

#優點 ：適合於改善影象的區域性對比度以及獲得更多的影像細節。
#缺點 ：在對比度增強的同時，也放大了影像的噪音，所以才需要下面會介紹的CLAHE均衡來改善噪聲放大的問題。

# read image
img = cv2.imread('wallpaper.jpg')

# convert the image into grayscale before doing histogram equalization
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# image equalization
equalize_img = cv2.equalizeHist(gray_img)

# create clahe image
clahe = cv2.createCLAHE()
clahe_img = clahe.apply(gray_img)

# show image
cv2.imshow("image", gray_img)
cv2.imshow("equal_image", equalize_img)
cv2.imshow("clahe_image", clahe_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plot image histogram 
plt.hist(gray_img.ravel(), 256, [0, 255],label= 'original image')
plt.hist(equalize_img.ravel(), 256, [0, 255],label= 'equalize image')
plt.hist(clahe_img.ravel(), 256, [0, 255],label= 'clahe image')
plt.legend()
