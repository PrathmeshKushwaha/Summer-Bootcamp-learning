from tkinter import *
import tkinter.messagebox
import SDMS_BE as BE
class student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg='cadet blue')
        self.root.grid_propagate(False)

        StdID = StringVar()
        f_name = StringVar()
        l_name = StringVar()
        Age = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
            return
        
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfname.delete(0,END)
            self.txtlname.delete(0,END)
            self.txtAge.delete(0,END)
        
        def addData():
            if (len(StdID.get()) != 0):
                BE.addrecord(StdID.get(), f_name.get(), l_name.get(), Age.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), f_name.get(), l_name.get(), Age.get()))
        
        def displaydata():
            studentlist.delete(0,END)
            for row in BE.viewdata():
                studentlist.insert(END,row,str("")) 

        def Studentrec(event):
            global stdID
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfname.delete(0,END)
            self.txtfname.insert(END,sd[1])
            self.txtlname.delete(0,END)
            self.txtlname.insert(END,sd[1])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[1])

        def deletedata():
            if(len(StdID.get()) != 0):
                BE.delete(sd[0])
                clearData()
                displaydata()
        
        def searchdata():
            studentlist.delete(0,END)
            for row in BE.search(StdID.get(), f_name.get(), l_name.get(), Age.get()):
                studentlist.insert(END,row,str(""))
        
        def updatedata():
            if(len(StdID.get()) != 0):
                BE.delete(sd[0])
            if(len(StdID.get()) != 0):
                BE.addrecord(StdID.get(), f_name.get(), l_name.get(), Age.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), f_name.get(), l_name.get(), Age.get()))


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

        self.lblStdID = Label(DataFrameLeft, font=('arial',20,'bold'), text="Student ID:",padx=2,pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0,column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLeft, font=('arial',20,'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0,column=1)

        self.lblfname = Label(DataFrameLeft, font=('arial',20,'bold'), text="First Name:",padx=2,pady=2, bg="Ghost White")
        self.lblfname.grid(row=1,column=0, sticky=W)
        self.txtfname = Entry(DataFrameLeft, font=('arial',20,'bold'), textvariable=f_name, width=39)
        self.txtfname.grid(row=1,column=1)

        self.lbllname = Label(DataFrameLeft, font=('arial',20,'bold'), text="Last Name:",padx=2,pady=2, bg="Ghost White")
        self.lbllname.grid(row=2,column=0, sticky=W)
        self.txtlname = Entry(DataFrameLeft, font=('arial',20,'bold'), textvariable=l_name, width=39)
        self.txtlname.grid(row=2,column=1)

        self.lblAge = Label(DataFrameLeft, font=('arial',20,'bold'), text="Age:",padx=2,pady=2, bg="Ghost White")
        self.lblAge.grid(row=3,column=0, sticky=W)
        self.txtAge = Entry(DataFrameLeft, font=('arial',20,'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=3,column=1)


        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1, sticky='NS')

        studentlist = Listbox(DataFrameRight, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=Scrollbar.set)
        studentlist.bind('<<ListBoxSelect>>', Studentrec)
        studentlist.grid(row=0,column=0, padx=8)
        scrollbar.config(command = studentlist.yview)


        self.btnAddData = Button(butFrame, text="Add new",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0,column=0)
        self.btnAddData = Button(butFrame, text="Display",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=displaydata)
        self.btnAddData.grid(row=0,column=1)
        self.btnAddData = Button(butFrame, text="Clear",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=clearData)
        self.btnAddData.grid(row=0,column=2)
        self.btnAddData = Button(butFrame, text="Delete",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=deletedata)
        self.btnAddData.grid(row=0,column=3)
        self.btnAddData = Button(butFrame, text="Search",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=searchdata)
        self.btnAddData.grid(row=0,column=4)
        self.btnAddData = Button(butFrame, text="Update",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=updatedata)
        self.btnAddData.grid(row=0,column=5)
        self.btnAddData = Button(butFrame, text="Exit",font=('arial', 20,'bold'), height=1,width=10, bd=4, command=iExit)
        self.btnAddData.grid(row=0,column=6)



if __name__== '__main__':
    root = Tk()
    application = student(root)
    root.mainloop()