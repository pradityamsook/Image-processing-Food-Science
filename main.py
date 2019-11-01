from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import cv2

#matplotlib inline
fileImage = cv2.imread('/pics/49994.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([fileImage], [i], None, [256], [0, 256]
    plt.plot(histr, color = col)
	plt.xlim([0,256])
plt.show()

class Contour:
    def __init__(self, fileName=None):
        self.fileName = fileName

    def detectContour(self):
        imgGray = cv2.cvtColor(self.fileName, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgGray, 100, 255, 0)
        contour, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.fileName, contour, -1, (0, 0, 255), 3)
   
    #def histroGram(self):
        #import matplotlib.pyplot as plt
        #for i, col in enumerate(['b', 'g', 'r']):
           # hist = cv2.calHist([self.filename], [i], None, [256], [0, 256]
            #plt.plot(hist, color = col)
            #plt.xlim([0, 256])
        #plt.show()

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
        cv2.imshow("ภาพก่อนประมวลผล", self.imgScaled)
        _Contour = Contour(self.img)
        _Contour.detectContour()
        self.imgScaled01 = cv2.resize(self.img, (720, 500), interpolation = cv2.INTER_AREA)
        cv2.imshow("ภาพหลังประมวลผล", self.imgScaled01)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        _Contour.histroGram()

root = Tk()
root.geometry("400x400")
root.title("Food Science Application")
app = Window(root)
root.mainloop()

