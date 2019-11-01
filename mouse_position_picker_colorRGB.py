import pyautogui as pag
import numpy as np
positionXY = pag.position()
print(positionXY, pag.pixel(positionXY[0], positionXY[1]))
while True:
    positionXY = pag.position()
    color = pag.pixel(positionXY[0], positionXY[1])
    npColor = np.array(color)
    print(npColor)

