import tkinter as tk

window = tk.Tk()
window.title("TextBox") 
window.geometry('400x200')

inputtxt = tk.Text(window, height = 5, width = 20) 
inputtxt.pack()

def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp)

printButton = tk.Button(window, text = "Print", command = printInput) 
printButton.pack()

lbl = tk.Label(window, text = "") 
lbl.pack() 

window.mainloop()