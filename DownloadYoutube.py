from tkinter import *
root = Tk()

my_label = Label(root, text = "Welcome to Clifford's Youtube Downloader")
my_label.pack()

root.mainloop()



# def Get_Ytube():


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
#     print("Downloading ...")
#     yt.download()
#     print("Downloading Complete, Thanks :)")


# Get_Ytube()   
