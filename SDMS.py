from tkinter import *
import tkinter.messagebox

class student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg='cadet blue')
        self.root.grid_propagate(False)

        stdID = StringVar()
        f_name = StringVar()
        l_name = StringVar()
        Age = StringVar()

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=50, pady=8, bg="Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 44, 'bold'), text='Student Database Management Systems',bg="Ghost White")
        self.lblTitle.grid()

        butFrame = Frame(MainFrame, bd=2 ,width=1366 ,height=70 ,padx=18, pady=10, bg="Ghost White", relief = RIDGE)
        butFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1 ,width=1316 ,height=400, padx=20, pady=20, bg="Cadet Blue", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1066 ,height=600,padx=20, bg="Ghost White", relief = RIDGE,
                                     font=('arial', 17, 'bold'), text="Student Info\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450 ,height=300,padx=31,pady=3, bg="Ghost White", relief = RIDGE,
                                    font=('arial', 17, 'bold'), text="Student Details\n")
        DataFrameRight.pack(side=RIGHT)

if __name__== '__main__':
    root = Tk()
    application = student(root)
    root.mainloop()