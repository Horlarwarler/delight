import tkinter as tk
from tkinter import messagebox


class Application():
    def __init__(self):
        self.root = tk.Tk()        
        self.height = 768
        self.width = 1366 
        self.root.geometry(f'{self.width}x{self.height}')

        self.root.config(background="#2148C0")
        self.root.title("Delight Supermarket")
        self.root.resizable(False, False)

    def loginWindow(self):

        self.loginLabel=tk.Label(self.root,text="Login User",font=('arial 18 bold'),fg='white',bg="#2148C0")
        self.loginLabel.place(x=600, y = 180)

        self.loginframe = tk.Frame(self.root,width=576,height=330, bg="#4361BE")
        

        self.usernameLabel = tk.Label(self.loginframe,text="Username",font=('arial 15 bold'),fg='white',bg="#4361BE")
        self.usernameLabel.place(x=55,y=30)

        self.userbox = tk.Entry(self.loginframe,width=35, font=('arial 18 bold'),bg="#F0FEF6")
        self.userbox.place(x=55,y=80)
        self.userbox.focus()

        self.passwordLabel=tk.Label(self.loginframe,text="Password",font=('arial 15 bold'),fg='white',bg="#4361BE")
        self.passwordLabel.place(x=55,y=130)
        
        self.passbox = tk.Entry(self.loginframe,width=35, font=('arial 18 bold'),bg="#F0FEF6", show="x")
        self.passbox.place(x=55,y=180)

        self.quit = tk.Button(self.loginframe,text="Quit",width=12,height=2,bg="#F0FEF6",command=self.quit)
        self.quit.place(x=55,y=230)

        self.login = tk.Button(self.loginframe,text="Login",width=12,height=2,bg="#F0FEF6",command=self.validateLogin)
        self.login.place(x=420,y=230)

        self.lbl_result = tk.Label(self.loginframe, text="", font=('arial', 18), bg="#4361BE")
        self.lbl_result.place(x=60,y=280)


        self.loginframe.place(x = 395,y= 219)
    
    def validateLogin(self):
        self.password = self.passbox.get()
        self.username = self.userbox.get()

        if(self.password == "" or self.username == ""):
            self.lbl_result.config(text="Please complete the required field!", fg="red")
        elif(self.password == "root" and self.username == "admin"):
            self.mainWindow()

            self.root.withdraw()
            
        else:
            self.lbl_result.config(text="Incorrect Username or Password", fg="red")
        self.userbox.delete(0, tk.END)
        self.passbox.delete(0, tk.END)

    def mainWindow(self):
        self.userDBoard = tk.Toplevel()
        self.userDBoard.geometry(f'{self.width}x{self.height}')
        self.userDBoard.config(background="#2148C0")
        self.userDBoard.resizable(False, False)
        self.userDBoard.protocol("WM_DELETE_WINDOW", self.quitApplication)


        topHeader = tk.Label(self.userDBoard)
        topHeader.place(x=0, y=0, height=64, width=283)
        topHeader.configure(
            activebackground = "#4e63f3",
            activeforeground = "white",
            anchor = 'w',
            background = "#4e63f3",
            #585858
            foreground = "#ffffff",
            text = 'DELIGHT',
            disabledforeground = "#a3a3a3",
            font = "-family {Segoe UI} -size 13 -weight bold",
            compound = 'right',
            padx = "100",
            pady = "10"
        )

        self.HeadingRight = tk.Frame(self.userDBoard)
        self.HeadingRight.place(x=280, y=0, height=64, width=1085)
        self.HeadingRight.configure(
            relief="groove",
            background="#0000a0"
        )

        self.MenuFrame = tk.Frame(self.userDBoard)
        self.MenuFrame.place(x=0, y=64, height=703, width=281)
        self.MenuFrame.configure(relief="groove")
        self.MenuFrame.configure(background="#585858")

        self.currentToolIndicator = tk.Frame(self.userDBoard, background="#c0c0c0", relief="groove")
        self.currentToolIndicator.place(x = 280, y=64, height=50, width=1085)

        self.CurrentToolLabel = tk.Label(self.currentToolIndicator)
        self.CurrentToolLabel.place(relx=0.009, rely=0.0, height=50, width=144)
        self.CurrentToolLabel.configure(
            anchor='w',
            background="#c0c0c0",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 15 -weight bold",
            foreground="#3f3f3f",
            text='''Dashboard'''
        )

        self.Container = tk.Frame(self.userDBoard)
        self.Container.place(x=280, y=114, height=653, width=1085)
        self.Container.configure(relief="groove")
        self.Container.configure(background="#c0c0c0")

        

        # Addin
        self.toolList = {
            "Dashboard": (lambda:self.switchTool("Dashboard", self.dashboard)),
            'Category': (lambda:self.switchTool('Category', self.category)),
            'Orders': (lambda:self.switchTool('Orders', self.order)),
            'Report': (lambda:self.switchTool('Report', self.report))
        }
        self.toolButton = {}
        x = 0
        y = 50
        for btnName, func in self.toolList.items():
            btn = tk.Button(self.MenuFrame, text=btnName, command=func)
            btn.configure(
                activebackground="#000000",
                activeforeground="white",
                background="#008080",
                compound='left',
                cursor="arrow",
                disabledforeground="#a3a3a3",
                font="-family {Segoe UI} -size 18",
                foreground="#ffffff",
                highlightbackground="#d9d9d9",
                highlightcolor="black",
                pady="0"
            )
            btn.place(x=x, y=y, height=54, width=281)
            self.toolButton[btnName] = btn
            y += 80

        self.Logout = tk.Button(self.MenuFrame,command=self.logout)
        self.Logout.place(x=67, y=590, height=54, width=147)
        self.Logout.configure(
            activebackground="#000000",
            activeforeground="white",
            foreground="#ffffff",
            background="#ff0000",
            compound='left',
            cursor="X_cursor",
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 18",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            pady="0",
            text='''Log Out'''
        )

        self.currentToolbutton = self.toolButton['Dashboard']
        self.switchTool("Dashboard", self.dashboard)

    def dashboard(self):    
        Items = tk.Frame(self.Container)
        Items.place(relx=0.009, rely=0.071, relheight=0.178, relwidth=0.226)    
        Items.configure(relief="groove")
        Items.configure(background="#8000ff")

        totalItemLabel = tk.Label(Items)
        totalItemLabel.place(relx=0.041, rely=0.48, height=41, width=124)
        totalItemLabel.configure(
            anchor='w',
            background="#8000ff",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff",
            text='''Total Items'''
        )   
        
        totalItemCount = tk.Label(Items)
        totalItemCount.place(relx=0.041, rely=0.16, height=41, width=124)
        totalItemCount.configure(
            activebackground="#f9f9f9",
            activeforeground="black",
            anchor='w',
            background="#8000ff",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 24 -weight bold",
            foreground="#ffffff",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''20'''
        )

        categorycount = tk.Frame(self.Container)
        categorycount.place(relx=0.276, rely=0.071, relheight=0.178, relwidth=0.226)
        categorycount.configure(
            relief="groove",
            background="#008040",
            highlightbackground="#d9d9d9",
            highlightcolor="black"
        )

        categoryCountLabel = tk.Label(categorycount)
        categoryCountLabel.place(relx=0.041, rely=0.48, height=41, width=124)
        categoryCountLabel.configure(
            activebackground="#f9f9f9",
            activeforeground="black",
            anchor='w',
            background="#008040",
            borderwidth="0",
            compound='left',
            cursor="fleur",
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Category'''
        )

        categoryCountl = tk.Label(categorycount)
        categoryCountl.place(relx=0.041, rely=0.16, height=41, width=124)
        categoryCountl.configure(
            activebackground="#f9f9f9",
            activeforeground="black",
            anchor='w',
            background="#008040",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 24 -weight bold",
            foreground="#ffffff",
            highlightbackground="#d9d9d9",
            text='''14'''
        )

        categorycount_1 = tk.Frame(self.Container)
        categorycount_1.place(relx=0.553, rely=0.071, relheight=0.178, relwidth=0.226)
        categorycount_1.configure(
            relief="groove",
            background="#008040",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
        )

        paidCountLabel = tk.Label(categorycount_1)
        paidCountLabel.place(relx=0.041, rely=0.48, height=41, width=124)
        paidCountLabel.configure(
            activebackground="#f9f9f9",
            activeforeground="black",
            anchor='w',
            background="#008040",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Paid Orders'''
        )

        paidCount = tk.Label(categorycount_1)
        paidCount.place(relx=0.041, rely=0.16, height=41, width=124)
        paidCount.configure(
            activebackground="#f9f9f9",
            activeforeground="black",
            anchor='w',
            background="#008040",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 24 -weight bold",
            foreground="#ffffff",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''30'''
        )

    def order(self):
        pass

    def category(self):
        addButton = tk.Button(self.Container,background="#458afc", width = 15 ,height=2,text="Add categroy",font="-family {Segoe UI} -size 10 -weight bold" )
        addButton.place(x = 0 , y = 50)
        
    def report(self):
        pass

    def switchTool(self, toolName, func):
        self.CurrentToolLabel.config(text=toolName)
        self.currentToolbutton.config(state=tk.NORMAL)
        self.currentToolbutton = self.toolButton[toolName]
        self.currentToolbutton.config(state=tk.DISABLED)

        for wid in self.Container.winfo_children():
            wid.destroy()

        func()

    def quit(self):        
        if messagebox.askyesno("Quit Application", message="Dont be silly boss"):
            self.root.destroy()
            exit()
    
    def quitApplication(self):
        if messagebox.askyesno("Simple Inventory System", message="Quit Application?"):
            self.userDBoard.destroy()
            self.root.destroy()
            exit()

    def logout(self,*args,**kwargs):
        result = messagebox.askquestion('Simple Inventory System', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes':         
            self.root.deiconify()
            self.userDBoard.destroy()

    

    def run(self):
        self.loginWindow()

        self.root.mainloop()


Application().run()    

