""" อ่านก่อนทำความเข้าใจโค้ด """
""" ' ### messages ### ' That mean big warnings. """
""" ' # messages ' That mean normal comment of codes. """
""" If have commnet no full stop (.), that code is commented."""

from tkinter import *
from tkinter import filedialog
from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont
#from matplotlib import pyplot as plt
import numpy as np
import cv2

### Don't touch this comment. ###
""" fileImage = cv2.imread('/pics/49994.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([fileImage], [i], None, [256], [0, 256]
    plt.plot(histr, color = col)
	plt.xlim([0,256])
plt.show()
 """
class Contour:
    def __init__(self, fileName=None):
        self.fileName = fileName

    def detectContour(self):
        imgGray = cv2.cvtColor(self.fileName, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgGray, 100, 255, 0)
        contour, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.fileName, contour, -1, (0, 0, 255), 3)
################################

### Don't touch this comment. ###
""" class CountColorRatio:
    def __init__(self, file=None):
        self.file = file

    def RatioMeatAndFat(self):
        img_I = Image.open(self.file)
        fat = 0
        meat = 0

        for fat_I in list(img_I):
            if fat_I <= (210, 230, 210) and fat_I >= (150, 135, 105):
                fat += 1
            if fat_I >= (40, 30, 25) and fat_I <= (175, 100, 70):
                meat += 1

        sumPixelMeat = fat + meat
        ratioMeat = (100 / sumPixelMeat) * meat
        ratioFat = (100 / sumPixelMeat) * fat
        fontType = ImageFont.truetype('Arial.tff', 20)
        draw = ImageDraw.Draw(img_I)
        draw.text(xy = (0, 0), text = 'Meat ' + ratioMeat + '%', fill = (0, 0, 0), font = fontType)
        draw.text(xy = (0, 20), text = 'Fat ' + ratioFat + '%', fill = (0, 0, 0), font = fontType)
        img_I.save("C:/Users/output.jpg") """

    #def histroGram(self):
        #import matplotlib.pyplot as plt
        #for i, col in enumerate(['b', 'g', 'r']):
           # hist = cv2.calHist([self.filename], [i], None, [256], [0, 256]
            #plt.plot(hist, color = col)
            #plt.xlim([0, 256])
        #plt.show()
################################

class Window:
    def __init__(self, master):
        self.master = master
        #self.init_window()
        openFileButton = Button(master, text = "เลือกรูปภาพ", command=self.open_file_name)
        openFileButton.place(x = 0, y = 0)

    def open_file_name(self):
        self.filename = filedialog.askopenfilename(
							initialdir = "/", 
							title = "Select file", 
							filetypes = (
								(
									"jpeg files", 
									"*.jpg"
								), 
								(
									"all files", 
									"*.*"
								)
							)
						)
        print(self.filename)

        self.img = cv2.imread(self.filename)
        #cv2.imshow("รูปภาพ ", self.img)
        self.imgScaled = cv2.resize(self.img, (720, 500), interpolation = cv2.INTER_AREA)
        cv2.imwrite("C:/Users/output1.png", self.imgScaled)
        #cv2.imshow("ภาพก่อนประมวลผล", self.imgScaled)
       # _Contour = Contour(self.img)
       # _Contour.detectContour()
        #self.imgScaled01 = cv2.resize(self.img, (720, 500), interpolation = cv2.INTER_AREA)
        img_I = Image.open(r"C:/Users/output1.png").getdata
        img_I01 = Image.Image.getdata(img_I)
        fat = 0
        meat = 0

        for fat_I in list(int(img_I01)):
            if fat_I <= (210, 230, 210) and fat_I >= (150, 135, 105): #condition find fat(white).
                fat += 1
            if fat_I >= (40, 30, 25) and fat_I <= (175, 100, 70): #condition find meat(red).
                meat += 1

        sumPixelMeat = fat + meat
        ratioMeat = (100 / sumPixelMeat) * meat #find ratio meat.
        ratioFat = (100 / sumPixelMeat) * fat #find ratio fat.
        
        """ Show text image of this process
        example: Meat 79%
                 fat 21%
        """
        fontType = ImageFont.truetype('arial.ttf', 20)
        draw = ImageDraw.Draw(img_I)
        draw.text(xy = (0, 0), text = 'Meat ' + ratioMeat + '%', fill = (0, 0, 0), font = fontType)
        draw.text(xy = (0, 20), text = 'Fat ' + ratioFat + '%', fill = (0, 0, 0), font = fontType)
        img_I01.show()
        """ ////////////////////////////////////////////////////////////////////////////////////// """

        #cv2.imshow("Processed", self.imgScaled)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #_Contour.histroGram()

root = Tk()
root.geometry("400x400")
root.title("Food Science Application")
app = Window(root)
root.mainloop()

