from tkinter import *

win = TK()
win.geometry("700x250")

def open_text():
   text_file = open("test.txt", "r")
   content = text_file.read()
   my_text_box.insert(END, content)
   text_file.close()