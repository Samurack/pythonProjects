import tkinter as tk
from tkvideo import tkvideo
import os
import time
from tkinter import *
from PIL import Image
from PIL import ImageTk
import imageio
import vlc


path =r'D:\code\slideShow'
list_of_files = []
photos = []
same = True
#n can't be zero, recommend 0.25-4
n=0.9

# adjust window
rootofSystem=tk.Tk()
rootofSystem.geometry("500x500")
l=Label()
l.pack()
media_player = vlc.MediaPlayer()

for root, dirs, files in os.walk(path):
    for file in files:
        if('.jpg' in file): #https://stackoverflow.com/questions/4066202/resizing-pictures-in-pil-in-tkinter/32803004
            # list_of_files.append(os.path.join(root,file))
            tempimage = Image.open(os.path.join(file))
            [imageSizeWidth, imageSizeHeight] = tempimage.size
            while imageSizeWidth > 500 and imageSizeHeight > 500: #https://stackoverflow.com/questions/1729887/little-math-help-for-image-resize-needed
                imageSizeWidth = int(imageSizeWidth * n)
                imageSizeHeight = int(imageSizeHeight * n) 
                tempimage = tempimage.resize((imageSizeHeight, imageSizeHeight), Image.ANTIALIAS)
            list_of_files.append(ImageTk.PhotoImage(tempimage))
        elif('.mp4' in file):
            media = vlc.Media(os.path.join(file)) #https://www.geeksforgeeks.org/python-vlc-mediaplayer-setting-play-rate/
            list_of_files.append(media)

# using recursion to slide to next image
x = 0

def move():
    global x
    # print(type(list_of_files[x]))
    if x > len(list_of_files)-1:
        x = 0
    if isinstance(list_of_files[x], tkvideo): #https://www.geeksforgeeks.org/python-vlc-mediaplayer-setting-play-rate/
        # list_of_files[x].play()
        # setting media to the media player
        media_player.set_media(list_of_files[x])
        media_player.play()
        time.sleep(5)

    else:
        l.config(image=list_of_files[x])
    x = x+1
    rootofSystem.after(2000, move)

move() 

rootofSystem.mainloop()