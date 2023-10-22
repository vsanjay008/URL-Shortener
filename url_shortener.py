from tkinter import *
import pyshorteners
import pyperclip
from pyshorteners.exceptions import ShorteningErrorException

root = Tk()
root.title("Url Shortener")
root.geometry("420x250")
root.configure(bg="lightgrey")
URL = StringVar()

head = Label(root,text="URL Shortener",font=(20))
head.grid(row=0,column=1,padx=150,pady=10)

def urlshortener():
    long_url = URL.get()
    if long_url:
        short = pyshorteners.Shortener()
        try:
            result = short.tinyurl.short(long_url)
            show(result)
        except ShorteningErrorException as e:
            show(f"An error occurred: {e}")
    else:
        show("Please enter a URL")

Url = Entry(root,textvariable=URL,font=(20))
Url.grid(row=1,column=1,padx=50,pady=10)

submit = Button(root,text="Generate Short Url",font=(20),command=urlshortener)
submit.grid(row=3,columnspan=3)

result_label = Label(root, text="", font=(None, 12))
result_label.grid(row=4, column=1, pady=10)

def show(result):
    result_label.config(text=result)
    copy_button.config(state=NORMAL)  

def copy():
    shortened_url = result_label.cget("text")  
    pyperclip.copy(shortened_url)

copy_button = Button(root, text="Copy URL", font=(None, 16), state=DISABLED, command=copy)
copy_button.grid(row=5, column=1, pady=10)

root.mainloop()