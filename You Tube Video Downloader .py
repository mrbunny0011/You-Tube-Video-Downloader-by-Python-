# You Tube Video Downloader
from tkinter import *
from pytube import YouTube
from tkinter import messagebox,ttk,filedialog

# Function for Download Video
def downloder():
    link=down.get()
    download_folder=path.get()
    if link != "" and download_folder != "":
        try:
            yt=YouTube(link)
            video=yt.streams.get_highest_resolution()
            video.download(download_folder)
            messagebox.showinfo(title='Information', message=f'Video Downloaded successfully to {download_folder}')
        except:
            messagebox.showwarning(title='Warning!',message='Your Video is Not Found ')
            
    else:
        messagebox.showwarning(title='Warning!',message='Pleace Enter URL ')
 
# Function for Browse your place
def browse():
    downlode_directory=filedialog.askdirectory(initialdir="your directory path",title="Save Video")
    path.set(downlode_directory)
    

# Tkinter Function    
root=Tk()
root.title("Video Downloader")
root.geometry("630x400")
root.configure(bg='#A0522D')

# First Hading
text_hading=Label(root,text="You Tube Video Downloader ",bg='#A0522D',fg="black")
text_hading.grid(row=0,column=0,columnspan=5,pady=(15,10),padx=(140,15))
text_hading.config(font=('vardana',17,'bold'))

text_path=Label(root,text="Select Your Place",bg='#A0522D',fg="white")
text_path.grid(row=1,column=0,columnspan=2,padx=(15,25))
text_path.config(font=('vardana',15))

path=StringVar()
save_path=Entry(root,width=40,textvariable=path,font=("vardana",10))
save_path.grid(row=1,column=3,columnspan=5,padx=(0,5))

btn_browse=Button(text="Browse",bg='#E56717',fg="white",width=10,height=1,font=("vardana",10,'bold'),command=browse)
btn_browse.grid(row=1,column=9,columnspan=2,padx=(10,15),pady=(15,10))

text_enter=Label(root,text="You Tube Video URL",bg='#A0522D',fg="white")
text_enter.grid(row=3,column=0,columnspan=2,padx=(15,15),pady=(15,0))
text_enter.config(font=('vardana',15))

down=StringVar()
entry=Entry(root,width=50,textvariable=down,font=("vardana",10))
entry.grid(row=3,column=3,columnspan=7,padx=(0,5),pady=(15,10))

btn_downloade=Button(text="Downloade",bg='#FF6700',fg="white",width=15,height=2,font=("vardana",10,'bold'),command=downloder)
btn_downloade.grid(row=4,column=0,columnspan=5,padx=(135,15),pady=(15,10))

root.mainloop()