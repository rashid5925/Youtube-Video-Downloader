import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox
from tkinter import PhotoImage
import threading


link = ""
title = ""
views = ""
def get_info():
    button["state"] = "disabled"
    button1["state"] = "disabled"
    views_l["text"] = ""
    title_l["text"] = ""
    link = link_field.get()
    try:
        yt = YouTube(link)

        title_l["text"] = "Title: " + str(yt.title)
        views_l["text"] = "Views: " + str(yt.views)
    except:
        title_l["text"] = "Video Not found"
        views_l["text"] = ""
    pb.stop()
    button["state"] = "normal"
    button1["state"] = "normal"


def get_info_thread():
    pb.start()
    t2 = threading.Thread(target=get_info)
    t2.start()
    

def download_video():
    
    if box.get() == "" or link_field.get() == "":
        pb.stop()
        messagebox.showerror("ERROR", "Fill All Fields")
        return
    link = link_field.get()
    button["state"] = "disabled"
    button1["state"] = "disabled"
    try:
        yt = YouTube(link)
        if box.get() == "Low Resolution":
            yd = yt.streams.get_lowest_resolution()
            yd.download()
        elif box.get() == "Audio Only":
            yd = yt.streams.get_audio_only()
            yd.download()
        else:
            yd = yt.streams.get_highest_resolution()
            yd.download()
    except:
        title_l["text"] = "Video Not found"
        views_l["text"] = ""
    pb.stop()
    messagebox.showinfo("Message", "Download Completed")
    button["state"] = "normal"
    button1["state"] = "normal"

def download_thread():
    pb.start()
    t2 = threading.Thread(target=download_video)
    t2.start()


window = tk.Tk()

window.title("YouTube Downloader")
window.geometry("700x400")

img = PhotoImage(file="logo.png")
window.wm_iconphoto(True, img)

window.grid()


link_label = tk.Label(window, text="Enter Link:", font=("Arial", 18), fg="Black")
link_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)


link_field = tk.Entry(window, font=("Arial", 12), width=60)
link_field.grid(column=1, row=0, sticky=tk.E, ipady=5, padx=5)

button = tk.Button(window, text="Get Video", font=("Arial", 20),
    bg="#eb9834", command=get_info_thread)
button.grid(column=1, row=1, ipady=5, ipadx=5, pady=20, padx=30)

title_l = tk.Label(window, text=title, font=("Arial", 12), fg="Blue")
title_l.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

views_l = tk.Label(window, text=views, font=("Arial", 12), fg="Blue")
views_l.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

res_l = tk.Label(window, text="Resolutions:", font=("Arial", 18), fg="Black")
res_l.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

resol = ["Low Resolution", "High Resolution", "Audio Only"]

box = ttk.Combobox(window, values=resol, width=40, font=("Arial", 12))
box.grid(row=4, column=1, padx=5, pady=5 ,ipady=5, ipadx=5)

button1 = tk.Button(window, text="Download", font=("Arial", 20),
    bg="#eb9834", command=download_thread)
button1.grid(column=1, row=5, ipady=5, ipadx=5, pady=20, padx=30)


pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
pb.grid(column=1, row=6, columnspan=2, padx=10, pady=20)


window.mainloop(0)
