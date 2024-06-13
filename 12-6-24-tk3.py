import tkinter as tk
import tkinter.messagebox
# program to create a pop up

window = tk.Tk() 
window.title("When you press a button the message will pop up") 
window.geometry('500x300') 

# Create a messagebox showinfo 
def onClick(): 
	tkinter.messagebox.showinfo("Welcome", "Hi I'm your pop up") 
 
button = tk.Button(window, text="Click Me", command=onClick, height=5, width=10) 

button.pack(side='bottom') 
window.mainloop()
