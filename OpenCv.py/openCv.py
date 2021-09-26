import cv2 
import numpy as np

imagen = cv2.imread('pika.png')
kernel = np.ones((5,5), np.uint8)
Canny = cv2.Canny(imagen, 225, 225)
Dialation = cv2.dilate(Canny, kernel, iterations=1)
Eroded = cv2.erode(Dialation,kernel,iterations=1)
img = cv2.resize(imagen,(200,250))
imggris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imshare = cv2.resize(imggris,(210,260))
imgdilation = cv2.resize(Dialation,(220,270))
imgrec=cv2.rectangle(imagen,(100,900),(500,300),(0,0,255))
imgredr = cv2.resize(imgrec,(150,200))
imgcanny = cv2.resize(Canny,(155,205))
imgeroded = cv2.resize(Eroded,(155,205))

cv2.imshow("imagen", img)
cv2.imshow("Gris", imshare)
cv2.imshow("Bordeado", imgdilation)
cv2.imshow("Rectángulo", imgredr)
cv2.imshow("Canny", imgcanny)
cv2.imshow("Eroded", imgeroded)
cv2.waitKey(0)
