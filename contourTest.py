import numpy as np
import cv2

from PIL import Image

img_I = Image.open("C:/Users/Public/Documents/Image-processing-Food-Science/pics/49994.jpg").getdata()
fat = 0
meat = 0
for fat_I in list(img_I):
    if fat_I <= (210, 230, 210) and fat_I >= (150, 135, 105):
        fat += 1
    if fat_I >= (40, 30, 25) and fat_I <= (175, 100, 70):
        meat += 1
print(fat)
print(meat)
#pathImage = 'C:\Users\IONIC\Documents\Image-processing-Food-Science\pics\49994.jpg'
""" image = cv2.imread("C:/Users/IONIC/Documents/Image-processing-Food-Science/pics/49994.jpg")
#blurred_frame = cv2.GaussianBlur(image, (5, 5), 0)
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowerMeatColor = np.array([5, 55, 55])
upperMeatColor = np.array([50, 55, 205])
mask = cv2.inRange(HSV, lowerMeatColor, upperMeatColor)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for count in contours:
    cv2.drawContours(image, count, -1, (255, 0, 0), 10)
cv2.imwrite('C:/Users/IONIC/Documents/Image-processing-Food-Science/pics/output/output.png', image) """