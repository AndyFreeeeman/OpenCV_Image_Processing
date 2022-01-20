#閾值分割-THRESH_OTSU優化演算法

src = cv2.imread(r'wallpaper.jpg', cv2.IMREAD_GRAYSCALE)

triThe = 0
maxval = 255
triThe, dst_tri = cv2.threshold(src, triThe, maxval, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
triThe1, dst_tri1 = cv2.threshold(src, triThe, maxval, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
print (triThe)
print (triThe1)
cv2.imshow("image", src)
cv2.imshow('thresh_out', dst_tri)
cv2.imshow('thresh_out1', dst_tri1)
cv2.waitKey(0)
cv2.destroyAllWindows()
