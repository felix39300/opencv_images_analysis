import cv2
import numpy as np

img = cv2.imread("ressources/macron.png")
kern = np.ones((5,5), np.uint8) ##values from 0 to 255
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgCanny1 = cv2.Canny(img,100,200)
imgCanny2 = cv2.Canny(img,200,100)
imgDialation = cv2.dilate(imgCanny,kern, iterations=1) ##Increase sizes of the edges
imgEroded = cv2.erode(imgDialation,kern, iterations=1) ##Decrase sizes of the edges


#cv2.imshow("Gray Image", imgGray)
#cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erroded Image", imgEroded)

cv2.waitKey(0)
