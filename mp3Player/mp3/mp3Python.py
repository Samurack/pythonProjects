import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system
import filetype #https://pypi.org/project/filetype/
import random

music_player = tkr.Tk() 
music_player.title("Life In Music") 
music_player.geometry("450x650")

directory = askdirectory()
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
pos = 0
for item in song_list:
    kind = str(filetype.guess(item))
    if "filetype.types.audio.Mp3" in kind:
        play_list.insert(pos, item)
        pos += 1
    else:
        song_list.remove(item)
pos = 0
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.08) #https://stackoverflow.com/questions/43034494/changing-volume-in-pygame-mixer-almost-no-effect
pygame.mixer.music.load(song_list[pos])

def startup():
    global pos
    pygame.mixer.music.load(song_list[pos])
    var.set(song_list[pos])
    pygame.mixer.music.play()
    pygame.mixer.music.pause() #https://stackoverflow.com/questions/25221036/pygame-music-pause-unpause-toggle

def play():
    if pygame.mixer.music.get_busy() == 1:
        pygame.mixer.music.pause() #https://stackoverflow.com/questions/25221036/pygame-music-pause-unpause-toggle
    elif pygame.mixer.music.get_busy() == 0:
        pygame.mixer.music.unpause() #https://stackoverflow.com/questions/25221036/pygame-music-pause-unpause-toggle

def stop():
    pygame.mixer.music.stop()
    startup()

def nextsong():
    global pos
    if pos >= (len(song_list) - 1):
        pos = 0
    else:    
        pos += 1
    pygame.mixer.music.load(song_list[pos])
    var.set(song_list[pos])
    pygame.mixer.music.play()

def shufflesongs():
    global pos
    pygame.mixer.music.stop()
    checkFirstSong = song_list[0] 

    while song_list[0] == checkFirstSong: #make sure we don't get the same first song after a shuffle
        random.shuffle(song_list)
        
    pos = 0
    for item in song_list:
        play_list.delete(pos)
        play_list.insert(pos, item)
        pos += 1
    pos = 0
    pygame.mixer.music.load(song_list[pos])
    var.set(song_list[pos])
    pygame.mixer.music.play()

def VolumeUp():
    currentVolume = pygame.mixer.music.get_volume() #https://stackoverflow.com/questions/43034494/changing-volume-in-pygame-mixer-almost-no-effect
    if currentVolume <= 1 and currentVolume >= 0:
        currentVolume += 0.01
    print(currentVolume)
    pygame.mixer.music.set_volume(currentVolume) #https://stackoverflow.com/questions/43034494/changing-volume-in-pygame-mixer-almost-no-effect

def VolumeDown():
    currentVolume = pygame.mixer.music.get_volume() #https://stackoverflow.com/questions/43034494/changing-volume-in-pygame-mixer-almost-no-effect
    if currentVolume <= 1 and currentVolume >= 0.0134375:
        currentVolume -= 0.01
    print(currentVolume)
    pygame.mixer.music.set_volume(currentVolume) #https://stackoverflow.com/questions/43034494/changing-volume-in-pygame-mixer-almost-no-effect

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Play/Pause", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Next", command=nextsong, bg="green", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Shuffle", command=shufflesongs, bg="green", fg="white")
Button5 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="VolumeUp", command=VolumeUp, bg="green", fg="white")
Button6 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="VolumeDown", command=VolumeDown, bg="green", fg="white")

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
Button6.pack(fill="x")

play_list.pack(fill="both", expand="yes")
startup()
music_player.mainloop()