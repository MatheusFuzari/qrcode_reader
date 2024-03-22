import time, serial, sys, os, cv2
import tkinter as tk
from tkinter import *
from cv2 import *
from scipy import *
from numpy import array
from tkinter import ttk
try:
 import Tkinter
 import ttk
except ImportError:
 import tkinter as Tkinter
 import tkinter.ttk as ttk
from PIL import Image, ImageTk
import cv2
from pyzbar.pyzbar import decode
import json
import locale
import time
from datetime import datetime

# set locale to Brazil with pt-Br text return
locale.setlocale(locale.LC_ALL, "pt_BR")
today = datetime.now().strftime('%a')

# Config camera port and first parameters
camera_id = 0
delay = 1
window_name = 'OpenCV pyzbar'

alunos = {
    "Julia Meneses":["seg","ter","qua","qui","sex"],
    "Roberto Carlos":["seg","sex"]
}
print(alunos)
img = cv2.imread('gatinho.jpeg')
img_heigth, img_width, _ = img.shape
x = 50
y = 50

#Tkinter start screen
mGui = Tk()
mGui.geometry('600x600+0+0')
mGui.configure(background="Sky Blue")
mGui.state('zoomed')
camFrame = Frame(mGui, width=435, height=475)
camFrame.place(x=100, y=60)
infoFrame = Frame(mGui, width=600, height=475, bg='red')
infoFrame.place(x=600, y=60)


cap = cv2.VideoCapture(camera_id)
ret, frame = cap.read()

v1 = Label(camFrame, text="QrCode Video")
v1.place(x=-80, y=-2)

def dddd():
    ret, frame = cap.read()
    
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    nimg = ImageTk.PhotoImage(image=img)
    
    v1.n_img = nimg
    v1.configure(image=nimg)
    
    mGui.after(10, dddd)
dddd()
mGui.mainloop()