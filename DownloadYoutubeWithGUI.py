#start
from tkinter import *
from tkinter import messagebox
from webbrowser import get
root = Tk()

#Title, Icon, Size 

root.title("Youtube Downloader")
root.iconbitmap('Dload.ico')
root.geometry("700x350")

#Create Label for Window

my_label = Label(root, text = "Hello, Welcome to Clifford's Youtube Downloader ").pack()
my_label2 = Label(root, text= "Please Paste the URL from Youtube.com").pack()
gui_link = Entry(root, width = 50, fg = 'black' ).pack()

#Button and Entry Field

def user_click():
    messagebox.showinfo("Finishing Touches", "Thanks for waiting, the program is complete")

mybutton = Button(root, text = "Begin Download", command = user_click, padx = 15, pady = 10).pack()

root.mainloop()

# def get_ytube():
#     from pytube import YouTube
#     link = input("enter the link: ")
#     yt = YouTube(link)
#     #Get Title
#     print(yt.title)
#     #Get Thumbnail Image
#     print(yt.thumbnail_url)
#     #select stream resolution
#     yt = yt.streams.get_highest_resolution()
#     #or yt = yt.streams.first()
#     # for video in yt.streams:
#     #     print(video)

#     yt.download()


# # get_ytube()   
