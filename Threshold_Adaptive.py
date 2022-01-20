#閾值分割-自適應閾值分割

img = cv2.imread(r'wallpaper.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 43, 0.15)
cv2.imshow("image", img)
cv2.imshow('thresh_out', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
