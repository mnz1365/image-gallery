import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("900x550")
window.resizable(False, False)
window.title("images")

# my images source
mypath = r"C:\Users\mnz\Desktop\code\codes\python\imagegui\img"
myimages = os.listdir(mypath)
imageStatus = 0

# shows first image
myimage = Image.open(mypath+"\\"+ myimages[imageStatus])
myimage_resize = myimage.resize((700,350), Image.DEFAULT_STRATEGY)
myimage = ImageTk.PhotoImage(myimage_resize)
image_label = tk.Label(window, image=myimage)
image_label.place(x=98,y=25)

# button the previous image
def myPrevious():
    global imageStatus, image_label, myimage, myimage_resize
    
    
    
    if imageStatus < len(myimages) and imageStatus != 0:
        
        imageStatus = imageStatus - 1
        
    if imageStatus == len(myimages):
        imageStatus = imageStatus - 1
    if imageStatus == 0:
        imageStatus = len(myimages) - 1
    
    
    myimage = Image.open(mypath+"\\"+ myimages[imageStatus])
    myimage_resize = myimage.resize((700,350), Image.DEFAULT_STRATEGY)
    myimage = ImageTk.PhotoImage(myimage_resize)
    image_label = tk.Label(window, image=myimage)
    image_label.place(x=98,y=25)
    # for updating label
    state_label_function()

B = Button(window, text ="Previous", command = myPrevious)
B.place(x=365,y=450)

# button the next image
def myNext():
    global imageStatus, image_label, myimage, myimage_resize
    
    
    
    if imageStatus < len(myimages):
        
        imageStatus = imageStatus + 1
        
    if imageStatus == len(myimages):
        imageStatus = 0
    
    
    myimage = Image.open(mypath+"\\"+ myimages[imageStatus])
    myimage_resize = myimage.resize((700,350), Image.DEFAULT_STRATEGY)
    myimage = ImageTk.PhotoImage(myimage_resize)
    image_label = tk.Label(window, image=myimage)
    image_label.place(x=98,y=25)
    # for updating label
    state_label_function()
    


B = Button(window, text ="    Next    ", command = myNext)
B.place(x=445,y=450)

# this label shows number of picture example : 3 of 21 (picture number three)
def state_label_function():
    mytext = str(imageStatus+1)  +" of "+  str(len(myimages))
    state_label = tk.Label(window, text= mytext)    
    state_label.place(x=790,y=490)

# for showing this label
state_label_function()

# when n key pressed the active next picture
def nPress(event) :
    myNext()

# when b key pressed the active previous picture
def bPress(event):
    myPrevious()

# key press events
window.bind("<KeyPress-n>", nPress)
window.bind("<KeyPress-b>", bPress)
window.bind("<KeyPress-Right>", nPress)
window.bind("<KeyPress-Left>", bPress)


window.mainloop()