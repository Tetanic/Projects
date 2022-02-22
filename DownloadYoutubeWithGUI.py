#start
from tkinter import *
from tkinter import messagebox

root = Tk()

#Get and Download Youtube Video
def get_ytube(url_string):
    from pytube import YouTube
    link = url_string
    yt = YouTube(link)
    #Get Title
    print(yt.title)
    #Get Thumbnail Image
    print(yt.thumbnail_url)
    #select stream resolution
    yt = yt.streams.get_highest_resolution()
    #or yt = yt.streams.first()
    # for video in yt.streams:
    #     print(video)

    yt.download()


#Title, Icon, Size 

root.title("Youtube Downloader")
root.iconbitmap(r'Dload.ico')
root.geometry("700x400")

#Create Label for Window

my_label = Label(root, text = "Hello, Welcome to Clifford's Youtube Downloader ").pack()
my_label2 = Label(root, text= "Please Paste the URL from Youtube.com").pack()
gui_link = Entry(root, width = 50, fg = 'black' )

#Button and Entry Field

def user_click():
    url_string = gui_link.get()
    # print(gui_link.get())
    messagebox.showinfo("Finishing Touches", "Thanks for waiting, the program is complete")
    get_ytube(url_string)

mybutton = Button(root, text = "Begin Download", command = user_click, padx = 15, pady = 10).pack()





gui_link.pack()

root.mainloop()