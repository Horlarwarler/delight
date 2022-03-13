import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


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
            'Products': (lambda:self.switchTool('Products', self.product)),
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

    def product(self):

        productContainer = tk.Frame(self.Container)
        productContainer.place(x=0, y=0, height=703, width=1085)
        productContainer.configure(relief="groove")
        productContainer.configure(background="#c0c0c0")       
        
        addButton = Button(productContainer,background="#458afc", width = 15 ,height=2,text="Add Product",font="-family {Segoe UI} -size 10 -weight bold", command=self.addProducts )
        addButton.place(x = 10 , y = 10)

        productList = Frame(productContainer,height= 500, width = 1050, bg= "#f7f7f7")
        productList.place(x = 10, y = 60, )
        searchLabel=Label(productList,text="Search: ", font="-family {Segoe UI} -size 13 -weight bold",foreground ='#3f3f3f',background="#f7f7f7")
        searchLabel.place(x=730, y = 50)
        searchBox = Entry(productList,width=35,  font=('arial 13 bold'),bg="#ffffff", border=1)
        searchBox.place(x=800,y=50)

        productName=Label(productList,text="product Name: ", font="-family {Segoe UI} -size 12 -weight bold ",foreground ="#3f3f3f",background="#f7f7f7")
        productName.place(x=20, y=100)

        actionName=Label(productList,text="Action: ", font="-family {Segoe UI} -size 12 -weight bold ",foreground ="#3f3f3f",background="#f7f7f7")
        actionName.place(x=700, y=100)
        TSeparator1 = ttk.Separator(productList, orient='horizontal')
        TSeparator1.place(x= 0, y = 130 ,width= 1050, height=2)
    def addProducts(self):
        newProduct = tk.Frame(self.Container)
        newProduct.place(x=0, y=0, height=450, width=1085)
        newProduct.configure(relief="groove")
        newProduct.configure(background="#c0c0c0") 
        Label1 = Label(newProduct)
        Label1.place(x=10, y=0,)
       # Label1.place()
        Label1.configure(anchor='w')
        Label1.configure(background="#c0c0c0")
        Label1.configure(borderwidth="0")
        Label1.configure(compound='left')
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font="-family {Segoe UI} -size 15 -weight bold")
        Label1.configure(foreground="#3f3f3f")
        Label1.configure(text='''Add new Products''')
        additemContainer = Frame(newProduct,height= 600, width = 1050, bg= "#f7f7f7")
        additemContainer.place(x = 10, y = 50, )
        name_l=Label(additemContainer,text="Enter Product Name",font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        name_l.place(x=10,y=20)
        #userbox = Entry(loginframe,width=35, font=('arial 18 bold'),bg="#F0FEF6")
        name_e=Entry(additemContainer,width=50,font=('arial 12 bold') ,background="#f7f7f7" ,border=4)
        name_e.place(x=10,y=60)

        stock_l=Label(additemContainer,text="Enter Quantity",font=('-family {Segoe UI} -size 12  ') ,background="#f7f7f7")
        stock_l.place(x=10,y=100)
        stock_e = Entry(additemContainer, width=50, font=('-family {Segoe UI} -size 12 '),background="#f7f7f7", border=4)
        stock_e.place(x=10, y=140)

        cp_l = Label(additemContainer,  text="Enter Cost Price ", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        cp_l.place(x=10, y=180)
        cp_e = Entry(additemContainer, width=50 , font=('-family {Segoe UI} -size 12 '),background="#f7f7f7" ,border=4)
        cp_e.place(x=10, y=220)

        sp_l = Label(additemContainer,  text="Enter selling Price ", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        sp_l.place(x=10, y=260)
        sp_e = Entry(additemContainer, width=50 , font=('-family {Segoe UI} -size 12 '),background="#f7f7f7" ,border=4)
        sp_e.place(x=10, y=300)
        clearButton = Button(additemContainer,background="RED", width = 15 ,height=2,text="Add products",font="-family {Segoe UI} -size 10 -weight bold" , )
        clearButton.place(x = 750 , y =350 )
        saveButton = Button(additemContainer,background="GREEN", width = 15 ,height=2,text="Save",font="-family {Segoe UI} -size 10 -weight bold" , )
        saveButton.place(x = 900 , y = 350)

    def order(self):
        orderContainer = tk.Frame(self.Container)
        orderContainer.place(x=0, y=0, height=703, width=1085)
        orderContainer.configure(relief="groove")
        orderContainer.configure(background="#c0c0c0")       
        
        addButton = Button(orderContainer,background="#458afc", width = 15 ,height=2,text="Add New Order",font="-family {Segoe UI} -size 10 -weight bold", command=self.addProducts )
        addButton.place(x = 10 , y = 10)

        productList = Frame(orderContainer,height= 500, width = 1050, bg= "#f7f7f7")
        productList.place(x = 10, y = 60, )
        searchLabel=Label(productList,text="Search: ", font="-family {Segoe UI} -size 13 -weight bold",foreground ='#3f3f3f',background="#f7f7f7")
        searchLabel.place(x=730, y = 50)
        searchBox = Entry(productList,width=35,  font=('arial 13 bold'),bg="#ffffff", border=1)
        searchBox.place(x=800,y=50)

        productName=Label(productList,text="product Name: ", font="-family {Segoe UI} -size 12 -weight bold ",foreground ="#3f3f3f",background="#f7f7f7")
        productName.place(x=20, y=100)

        actionName=Label(productList,text="Action: ", font="-family {Segoe UI} -size 12 -weight bold ",foreground ="#3f3f3f",background="#f7f7f7")
        actionName.place(x=700, y=100)
        TSeparator1 = ttk.Separator(productList, orient='horizontal')
        TSeparator1.place(x= 0, y = 130 ,width= 1050, height=2)
    def addorders():
        pass
    
        
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

