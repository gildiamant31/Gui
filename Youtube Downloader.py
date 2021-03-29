from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Youtube video downloader")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

# enter link
link = StringVar()

Label(root, text=': הכנס את הקישור שלך כאן', font='arial 17 bold').place(x=120, y=70)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=110)


# function to download video

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='ההורדה בוצעה', font='arial 17').place(x=190, y=210)


Button(root, text='הורד', font='arial 17 bold', bg='pale violet red', padx=2, command=Downloader).place(x=220,
                                                                                                            y=150)

root.mainloop()