import tkinter as tk

m = tk.Tk()
m.title('Tkinter application')
# w = tk.Label(m, text='Hi! Prathmesh here')
# button = tk.Button(m, text='Stop', width=25, command=m.destroy)
# button.pack()
# w.pack()
tk.Label(m, text='First Name').grid(row=0)
tk.Label(m, text='Last Name').grid(row=1)
e1 = tk.Entry(m)
e2 = tk.Entry(m)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

var1 = tk.IntVar()
tk.Checkbutton(m, text='male', variable=var1).grid(row=2, sticky='w')
var2 = tk.IntVar()
tk.Checkbutton(m, text='female', variable=var2).grid(row=3)

v = tk.IntVar()
tk.Radiobutton(m, text='GfG', variable=v, value=1).grid(row=4)
tk.Radiobutton(m, text='MIT', variable=v, value=2).grid(row=5)

Lb = tk.Listbox()
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.grid(row=1,column=2)

m.mainloop()
