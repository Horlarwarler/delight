
from pyclbr import Class
from tkinter import *
from tkinter import messagebox
from turtle import width
import Homepage

import mysql.connector
from mysql.connector import Error
import tkinter.messagebox

from pyparsing import White



class Appliccation():


    global currentScreeen
    currentScreen = "Dashboard"
    def __init__(self,master,*args,**kwargs):
        self.master=master

        self.loginLabel=Label(master,text="Login User",font=('arial 18 bold'),fg='white',bg="#2148C0")
        self.loginLabel.place(x=600, y = 180)

        self.loginframe = Frame(master,width=576,height=330, bg="#4361BE")
        self.loginframe.place(x = 395,y= 219)
        self.usernameLabel=Label(self.loginframe,text="Username",font=('arial 15 bold'),fg='white',bg="#4361BE")
        self.usernameLabel.place(x=55,y=30)
        self.userbox = Entry(self.loginframe,width=35, font=('arial 18 bold'),bg="#F0FEF6")
        self.userbox.place(x=55,y=80)
        self.userbox.focus()
        self.passwordLabel=Label(self.loginframe,text="Password",font=('arial 15 bold'),fg='white',bg="#4361BE")
        self.passwordLabel.place(x=55,y=130)
        #self.passbox =PasswordInput(self.loginframe)
        self.passbox = Entry(self.loginframe,width=35, font=('arial 18 bold'),bg="#F0FEF6", show="x")
        self.passbox.place(x=55,y=180)
        self.passbox.focus()
        self.quit = Button(self.loginframe,text="Quit",width=12,height=2,bg="#F0FEF6",command=self.quit)
        self.quit.place(x=55,y=230)
        self.login = Button(self.loginframe,text="Login",width=12,height=2,bg="#F0FEF6",command=self.login)
        self.login.place(x=420,y=230)
        self.lbl_result = Label(self.loginframe, text="", font=('arial', 18), bg="#4361BE")
        self.lbl_result.place(x=60,y=280)

    

    def Home(self= None):
        global Homepage
        Homepage = Tk()
        Homepage.title("Delight Supermarket")
        Homepage.geometry("1366x768+0+0")
        Homepage.config(background="#2148C0")
        Homepage.resizable(False, False)
       
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        self.top = Homepage
        self.TopHeader = Label(self.top)
        self.TopHeader.place(x=0, y=0, height=64, width=283)
        self.TopHeader.configure(activebackground="#4e63f3")
        self.TopHeader.configure(activeforeground="white")
        self.TopHeader.configure(anchor='w')
        self.TopHeader.configure(background="#4e63f3")
        self.TopHeader.configure(compound='right')
        self.TopHeader.configure(disabledforeground="#a3a3a3")
        self.TopHeader.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.TopHeader.configure(foreground="#ffffff")
        self.TopHeader.configure(padx="100")
        self.TopHeader.configure(pady="10")
        self.TopHeader.configure(text='''DELIGHT''')

        self.menubar = Menu(Homepage,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        #top.configure(menu = self.menubar)

        self.HeadingRight = Frame(self.top)
        self.HeadingRight.place(x=280, y=0, height=65, width=1085)
        self.HeadingRight.configure(relief="groove")
        self.HeadingRight.configure(background="#0000a0")

        self.MenuFrame = Frame(self.top)
        self.MenuFrame.place(x=0, y=64, height=703, width=281)
        self.MenuFrame.configure(relief="groove")
        self.MenuFrame.configure(background="#585858")

        self.Dashboard = Button(self.MenuFrame )
        self.Dashboard.place(x=-60, y=50, height=54, width=347)
        self.Dashboard.configure(activebackground="#000000")
        self.Dashboard.configure(activeforeground="white")
        self.Dashboard.configure(activeforeground="#000000")
        self.Dashboard.configure(background="#008080")
        self.Dashboard.configure(compound='left')
        self.Dashboard.configure(cursor="arrow")
        self.Dashboard.configure(disabledforeground="#a3a3a3")
        self.Dashboard.configure(font="-family {Segoe UI} -size 18")
        self.Dashboard.configure(foreground="#ffffff")
        self.Dashboard.configure(highlightbackground="#d9d9d9")
        self.Dashboard.configure(highlightcolor="black")
        self.Dashboard.configure(pady="0")
        self.Dashboard.configure(text='''Dashboard''')

        self.Category = Button(self.MenuFrame)
        self.Category.place(x=-72, y=120, height=54, width=357)
        self.Category.configure(activebackground="#000000")
        self.Category.configure(activeforeground="white")
        self.Category.configure(activeforeground="#000000")
        self.Category.configure(background="#008080")
        self.Category.configure(compound='left')
        self.Category.configure(cursor="arrow")
        self.Category.configure(disabledforeground="#a3a3a3")
        self.Category.configure(font="-family {Segoe UI} -size 18")
        self.Category.configure(foreground="#ffffff")
        self.Category.configure(highlightbackground="#d9d9d9")
        self.Category.configure(highlightcolor="black")
        self.Category.configure(pady="0")
        self.Category.configure(text='''Category''')

        self.Orders = Button(self.MenuFrame)
        self.Orders.place(x=-80, y=200, height=54, width=367)
        self.Orders.configure(activebackground="#000000")
        self.Orders.configure(activeforeground="white")
        self.Orders.configure(activeforeground="#000000")
        self.Orders.configure(background="#008080")
        self.Orders.configure(compound='left')
        self.Orders.configure(cursor="arrow")
        self.Orders.configure(disabledforeground="#a3a3a3")
        self.Orders.configure(font="-family {Segoe UI} -size 18")
        self.Orders.configure(foreground="#ffffff")
        self.Orders.configure(highlightbackground="#d9d9d9")
        self.Orders.configure(highlightcolor="black")
        self.Orders.configure(pady="0")
        self.Orders.configure(text='''Orders''')

        self.Report = Button(self.MenuFrame)
        self.Report.place(x=-80, y=280, height=54, width=367)
        self.Report.configure(activebackground="#000000")
        self.Report.configure(activeforeground="white")
        self.Report.configure(activeforeground="#000000")
        self.Report.configure(background="#008080")
        self.Report.configure(compound='left')
        self.Report.configure(cursor="arrow")
        self.Report.configure(disabledforeground="#a3a3a3")
        self.Report.configure(font="-family {Segoe UI} -size 18")
        self.Report.configure(foreground="#ffffff")
        self.Report.configure(highlightbackground="#d9d9d9")
        self.Report.configure(highlightcolor="black")
        self.Report.configure(pady="0")
        self.Report.configure(text='''Report''')

        self.Logout = Button(self.MenuFrame,command=self.out)
        self.Logout.place(x=20, y=590, height=54, width=147)
        self.Logout.configure(activebackground="#000000")
        self.Logout.configure(activeforeground="white")
        self.Logout.configure(activeforeground="#000000")
        self.Logout.configure(background="#ff0000")
        self.Logout.configure(compound='left')
        self.Logout.configure(cursor="X_cursor")
        self.Logout.configure(disabledforeground="#a3a3a3")
        self.Logout.configure(font="-family {Segoe UI} -size 18")
        self.Logout.configure(foreground="#ffffff")
        self.Logout.configure(highlightbackground="#d9d9d9")
        self.Logout.configure(highlightcolor="black")
        self.Logout.configure(pady="0")
        self.Logout.configure(text='''Log Out''')
       

        self.Container = Frame(self.top)
        self.Container.place(x=280, y=60, height=703, width=1085)
        self.Container.configure(relief="groove")
        self.Container.configure(background="#c0c0c0")
               
        def dashboard():
            global currentScreeen
            currentScreeen = "Dashboard"
            self.Label1 = Label(self.Container)
            self.Label1.place(relx=0.009, rely=0.0, height=51, width=144)
            self.Label1.configure(anchor='w')
            self.Label1.configure(background="#c0c0c0")
            self.Label1.configure(borderwidth="0")
            self.Label1.configure(compound='left')
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 15 -weight bold")
            self.Label1.configure(foreground="#3f3f3f")
            self.Label1.configure(text='''Dashboard''')
    
            self.Items = Frame(self.Container)
            self.Items.place(relx=0.009, rely=0.071, relheight=0.178, relwidth=0.226)
    
            self.Items.configure(relief="groove")
            self.Items.configure(background="#8000ff")   
            self.TotalItemLabel = Label(self.Items)
            self.TotalItemLabel.place(relx=0.041, rely=0.48, height=41, width=124)
            self.TotalItemLabel.configure(anchor='w')
            self.TotalItemLabel.configure(background="#8000ff")
            self.TotalItemLabel.configure(borderwidth="0")
            self.TotalItemLabel.configure(compound='left')
            self.TotalItemLabel.configure(disabledforeground="#a3a3a3")
            self.TotalItemLabel.configure(font="-family {Segoe UI} -size 13 -weight bold")
            self.TotalItemLabel.configure(foreground="#ffffff")
            self.TotalItemLabel.configure(text='''Total Items''')    
            self.totalItemCount = Label(self.Items)
            self.totalItemCount.place(relx=0.041, rely=0.16, height=41, width=124)
            self.totalItemCount.configure(activebackground="#f9f9f9")
            self.totalItemCount.configure(activeforeground="black")
            self.totalItemCount.configure(anchor='w')
            self.totalItemCount.configure(background="#8000ff")
            self.totalItemCount.configure(borderwidth="0")
            self.totalItemCount.configure(compound='left')
            self.totalItemCount.configure(disabledforeground="#a3a3a3")
            self.totalItemCount.configure(font="-family {Segoe UI} -size 24 -weight bold")
            self.totalItemCount.configure(foreground="#ffffff")
            self.totalItemCount.configure(highlightbackground="#d9d9d9")
            self.totalItemCount.configure(highlightcolor="black")
            self.totalItemCount.configure(text='''20''')
    
            self.Categorycount = Frame(self.Container)
            self.Categorycount.place(relx=0.276, rely=0.071, relheight=0.178
                    , relwidth=0.226)
            self.Categorycount.configure(relief="groove")
            self.Categorycount.configure(background="#008040")
            self.Categorycount.configure(highlightbackground="#d9d9d9")
            self.Categorycount.configure(highlightcolor="black")
    
            self.CategoryCountLabel = Label(self.Categorycount)
            self.CategoryCountLabel.place(relx=0.041, rely=0.48, height=41
                    , width=124)
            self.CategoryCountLabel.configure(activebackground="#f9f9f9")
            self.CategoryCountLabel.configure(activeforeground="black")
            self.CategoryCountLabel.configure(anchor='w')
            self.CategoryCountLabel.configure(background="#008040")
            self.CategoryCountLabel.configure(borderwidth="0")
            self.CategoryCountLabel.configure(compound='left')
            self.CategoryCountLabel.configure(cursor="fleur")
            self.CategoryCountLabel.configure(disabledforeground="#a3a3a3")
            self.CategoryCountLabel.configure(font="-family {Segoe UI} -size 13 -weight bold")
            self.CategoryCountLabel.configure(foreground="#ffffff")
            self.CategoryCountLabel.configure(highlightbackground="#d9d9d9")
            self.CategoryCountLabel.configure(highlightcolor="black")
            self.CategoryCountLabel.configure(text='''Category''')

            self.categoryCount = Label(self.Categorycount)
            self.categoryCount.place(relx=0.041, rely=0.16, height=41, width=124)
            self.categoryCount.configure(activebackground="#f9f9f9")
            self.categoryCount.configure(activeforeground="black")
            self.categoryCount.configure(anchor='w')
            self.categoryCount.configure(background="#008040")
            self.categoryCount.configure(borderwidth="0")
            self.categoryCount.configure(compound='left')
            self.categoryCount.configure(disabledforeground="#a3a3a3")
            self.categoryCount.configure(font="-family {Segoe UI} -size 24 -weight bold")
            self.categoryCount.configure(foreground="#ffffff")
            self.categoryCount.configure(highlightbackground="#d9d9d9")
            self.categoryCount.configure(highlightcolor="black")
            self.categoryCount.configure(text='''14''')
    
            self.Categorycount_1 =Frame(self.Container)
            self.Categorycount_1.place(relx=0.553, rely=0.071, relheight=0.178
                    , relwidth=0.226)
            self.Categorycount_1.configure(relief="groove")
            self.Categorycount_1.configure(background="#008040")
            self.Categorycount_1.configure(highlightbackground="#d9d9d9")
            self.Categorycount_1.configure(highlightcolor="black")
    
            self.paidCountLabel = Label(self.Categorycount_1)
            self.paidCountLabel.place(relx=0.041, rely=0.48, height=41, width=124)
            self.paidCountLabel.configure(activebackground="#f9f9f9")
            self.paidCountLabel.configure(activeforeground="black")
            self.paidCountLabel.configure(anchor='w')
            self.paidCountLabel.configure(background="#008040")
            self.paidCountLabel.configure(borderwidth="0")
            self.paidCountLabel.configure(compound='left')
            self.paidCountLabel.configure(disabledforeground="#a3a3a3")
            self.paidCountLabel.configure(font="-family {Segoe UI} -size 13 -weight bold")
            self.paidCountLabel.configure(foreground="#ffffff")
            self.paidCountLabel.configure(highlightbackground="#d9d9d9")
            self.paidCountLabel.configure(highlightcolor="black")
            self.paidCountLabel.configure(text='''Paid Orders''')
    
            self.paidCount = Label(self.Categorycount_1)
            self.paidCount.place(relx=0.041, rely=0.16, height=41, width=124)
            self.paidCount.configure(activebackground="#f9f9f9")
            self.paidCount.configure(activeforeground="black")
            self.paidCount.configure(anchor='w')
            self.paidCount.configure(background="#008040")
            self.paidCount.configure(borderwidth="0")
            self.paidCount.configure(compound='left')
            self.paidCount.configure(disabledforeground="#a3a3a3")
            self.paidCount.configure(font="-family {Segoe UI} -size 24 -weight bold")
            self.paidCount.configure(foreground="#ffffff")
            self.paidCount.configure(highlightbackground="#d9d9d9")
            self.paidCount.configure(highlightcolor="black")
            self.paidCount.configure(text='''30''')

        dashboard()
            
        




    def login(self,*args,**kwargs):
        self.password = self.passbox.get()
        self.username = self.userbox.get()

        print(self.password)
        print(self.username)

        if(self.password == "" or self.username == ""):
            self.lbl_result.config(text="Please complete the required field!", fg="red")
        elif(self.password == "root" and self.username == "admin"):
            self.Home()

            self.master.withdraw()
            
        else:
            self.lbl_result.config(text="Incorrect Username or Password", fg="red")
        self.userbox.delete(0, END)
        self.passbox.delete(0, END)
      

    def quit(self,*args,**kwargs):
        result = messagebox.askquestion('Simple Inventory System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()   
    def out(self,*args,**kwargs):
        print("HELLLLLL")
        result = messagebox.askquestion('Simple Inventory System', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes': 
        
            root.deiconify()
            Homepage.destroy()
   

  
        
root = Tk()
Appliccation(root)

root.geometry("1366x768+0+0")
root.config(background="#2148C0")
root.title("Delight Supermarket")
root.resizable(False, False)
root.mainloop()