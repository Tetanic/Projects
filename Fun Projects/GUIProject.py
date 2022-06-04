from tkinter import *
root = Tk()

root.title("Youtube Downloader")
root.iconbitmap('Dload.ico')
root.geometry("500x500")

my_label = Label(root, text = "Hello, Welcome to Clifford's Youtube Downloader").pack()
my_label2 = Label(root, text= "Please Paste the URL from Youtube.com").pack()

root.mainloop()
