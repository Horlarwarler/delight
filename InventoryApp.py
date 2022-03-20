#from ast import Pass
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import datetime
import os
import shutil
#from turtle import width
#import numpy as np
#import pandas as pd
import calendar
#from datetime import datetime
#from fpdf import FPDF
#import matplotlib.pyplot as plt
#from matplotlib import rcParamsorrder

from database import PRODUCT, ORDER, REPORT, Product, TransactionOrder, Report

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
        self.passbox.bind('<Return>',self.validateLogin)

        self.quit = tk.Button(self.loginframe,text="Quit",width=12,height=2,bg="#F0FEF6",command=self.quit)
        self.quit.place(x=55,y=230)

        self.login = tk.Button(self.loginframe,text="Login",width=12,height=2,bg="#F0FEF6",command=self.validateLogin)
        self.login.place(x=420,y=230)

        self.lbl_result = tk.Label(self.loginframe, text="", font=('arial', 18), bg="#4361BE")
        self.lbl_result.place(x=60,y=280)


        self.loginframe.place(x = 395,y= 219)
    
    def validateLogin(self,event=None):
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
        date=datetime.datetime.now().date()
        date_l=Label(self.HeadingRight,text="Today's Date: "+str(date),font=('-family {Segoe UI} -size 13 -weight bold'),bg='#0000a0',fg='white')
        date_l.place(x=850,y=30)

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
            text=f'''{PRODUCT.totalRow}'''
        )

        totalTransaction = tk.Frame(self.Container)
        totalTransaction.place(relx=0.276, rely=0.071, relheight=0.178, relwidth=0.226)
        totalTransaction.configure(
            relief="groove",
            background="#008040",
            highlightbackground="#d9d9d9",
            highlightcolor="black"
        )

        totalTransactionLabel = tk.Label(totalTransaction)
        totalTransactionLabel.place(relx=0.041, rely=0.48, height=41, width=124)
        totalTransactionLabel.configure(
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
            text='''Transactions'''
        )

        totalTransactionl = tk.Label(totalTransaction)
        totalTransactionl.place(relx=0.041, rely=0.16, height=41, width=124)
        totalTransactionl.configure(
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
            text=f'''{REPORT.totalRow}'''
        )

        totalTransaction_1 = tk.Frame(self.Container)
        totalTransaction_1.place(relx=0.553, rely=0.071, relheight=0.178, relwidth=0.226)
        totalTransaction_1.configure(
            relief="groove",
            background="#008040",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
        )

        paidCountLabel = tk.Label(totalTransaction_1)
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

        paidCount = tk.Label(totalTransaction_1)
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
            text=f'''{ORDER.totalRow}'''
        )

    def product(self):

        self.productContainer = tk.Frame(self.Container)
        self.productContainer.place(x=0, y=0, height=703, width=1085)
        self.productContainer.configure(relief="groove")
        self.productContainer.configure(background="#c0c0c0")       
        
        addButton = Button(self.productContainer,background="#458afc", width = 15 ,height=2,text="Add Product",font="-family {Segoe UI} -size 10 -weight bold", command=self.addUpdateProducts )
        addButton.place(x = 10 , y = 10)

        productList = Frame(self.productContainer,height= 550, width = 1050, bg= "#f7f7f7")
        productList.place(x = 10, y = 50, )
        headingFrame = Frame(productList, background="#ffffff")
        headingFrame.place(x= 10,y= 55)
        headings = ["S/N", "Product Name","Supplier" , "Quantity","Cost Price","Selling Price"]
        
        for i in range(6):
            heading = Button(headingFrame,background="#c0c0c0", width = 16 ,height=1,text=headings[i],font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' )
            heading.grid(column=i , row = 0)
        
        TSeparator1 = ttk.Separator(productList, orient='horizontal')
        TSeparator1.place(x= 0, y = 95 ,width= 1050, height=2)
        
        allproduct = PRODUCT.readAllrows()

        global y
        y = 5
        
        global endingValue , startingValue, currentPage
        global previousButtonState ,nextButtonState
        startingValue = int(0)
        currentPage = int(1)
        endingValue = int(7) if len(allproduct) > 7 else len(allproduct)
        previousButtonState = 'disabled'
        nextButtonState = 'active'
        #startingValue = int(0)
        #endingValue = int(7)
        def showOrders():
            productDropDown = Frame(productList,width=1050,background="#f7f7f7", height= 400)
            productDropDown.place(x =0 , y = 100)
            global endingValue, startingValue, currentPage
            global previousButtonState ,nextButtonState
            
            
            global y

            def deleteProduct(id):
                if messagebox.askyesno("Remove Product", "Are you sure you want to perform the operation?"):
                    PRODUCT.deleteRow(data=id)
                    messagebox.showinfo("Remove Product", "Product removed from database!")
                    self.product()

                ## Delete product from database
                
            def updateProduct(name):
                self.addUpdateProducts(state="Update",item = name)
                pass
            
            #for r in range(startingValue, endingValue):
            productButtons = {}
            for r in range(startingValue, endingValue):
                
                itemContainer = Frame(productDropDown, width=830, height= 60,)
                itemContainer.place(x=10,y =y)
                itemContainer.configure(relief="groove")
                backgroundColor = "#F2F2F2" if r % 2==0 else "White"
                
                tableEntry = Button(itemContainer,background=backgroundColor, width = 16 ,height=2,text=str(r + 1),font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' ,foreground="Black")
                tableEntry.grid(column=0 ,row= 0 )

                for c in range(1, 6):
                    tableEntry = Button(itemContainer,background=backgroundColor, width = 16 ,height=2,text=allproduct[r][c],font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' ,foreground="Black")
                    tableEntry.grid(column=c ,row= 0 )

                edit = tk.Button(itemContainer,text="Edit",width=10,height=2,bg="Yellow",command=lambda r = r : updateProduct(name = allproduct[r]))

                edit.grid(column=6, row = 0,padx=10)

                delete = tk.Button(itemContainer,text="Delete",width=10,height=2,bg="Red", command= lambda r = r: deleteProduct(id=allproduct[r][0]))
                delete.grid(column=7, row = 0,padx= 20)
                
                y += 50
                
            def previousButton():
                global  startingValue, endingValue , y, currentPage
                endingValue =  startingValue 
                startingValue -= 7 
                currentPage -=1
                y = 5
                productDropDown.pack_forget()
                showOrders()
            def nextButton():
                global  startingValue, endingValue ,y, difference, currentPage
                difference = len(allproduct) - endingValue
                if(difference >= 7):
                    startingValue += 7
                    endingValue +=  7
                else:
                    startingValue  = endingValue  
                    endingValue += difference
                y = 5
                currentPage +=1
                productDropDown.pack_forget()
                showOrders()
                            
            if startingValue == 0:
                previousButtonState = 'disabled'
            else:
                previousButtonState = 'active'
            if endingValue >= len(allproduct):
                nextButtonState = 'disabled'
            else:
                nextButtonState = 'active'
            previousButton = Button(productList,bg = "#f7f7f7", state=previousButtonState , text="Previous",font=('-family {Segoe UI} -size 12 -weight bold '), command=previousButton)
            previousButton.place(x =850 , y = 475 )
            currentCount = Button(productList,bg = "#f7f7f7",state='disabled', width=3,border=0, text=str(currentPage),font=('-family {Segoe UI} -size 12 -weight bold '))
            currentCount.place(x =940 , y = 480 )
            nextButton = Button(productList,bg = "#f7f7f7",state=nextButtonState , text="Next",font=('-family {Segoe UI} -size 12 -weight bold '),command= nextButton)
            nextButton.place(x =990 , y = 475 )
        showOrders()

    def addUpdateProducts(self,state ="new",item = ["","","","","",""]):
        self.productContainer.destroy()
        topHeaderText = "Add new Products" if state == "new" else "Update exiting Product"

        productName = StringVar(value=item[1]) 
        supplier = StringVar(value=item[2])
        productQuantity = StringVar(value=item[3])
        productCp = StringVar(value=item[4])
        productSp = StringVar(value=item[5])
        
        confirmText = "Add Product" if state == "new" else "Update Product"
        textVariable = "Enter" if state =="new" else "Change"
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
        Label1.configure(text= topHeaderText)
        additemContainer = Frame(newProduct,height= 600, width = 1050, bg= "#f7f7f7")
        additemContainer.place(x = 10, y = 50, )
        name_l=Label(additemContainer,text=textVariable +" Product Name",font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        name_l.place(x=10,y=20)
        
        name_e=Entry(additemContainer,width=50, textvariable = productName,font=('-family {Segoe UI} -size 12') ,background="#f7f7f7" ,border=2)
        name_e.place(x=10,y=60)
        supplier_l=Label(additemContainer,text=textVariable +" Supplier Name",font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        supplier_l.place(x=500,y=20)
        
        supplier_e=Entry(additemContainer,width=50, textvariable = supplier,font=('-family {Segoe UI} -size 12') ,background="#f7f7f7" ,border=2)
        supplier_e.place(x=500,y=60)

        quantity_l=Label(additemContainer,text=textVariable +" Quantity",font=('-family {Segoe UI} -size 12  ') ,background="#f7f7f7")
        quantity_l.place(x=10,y=100)
        quantity_e = Entry(additemContainer, width=50, textvariable=productQuantity, font=('-family {Segoe UI} -size 12 '),background="#f7f7f7", border=2)
        quantity_e.place(x=10, y=140)

        costPrice_l = Label(additemContainer,  text= textVariable +" Cost Price ", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        costPrice_l.place(x=10, y=180)
        costPrice_e = Entry(additemContainer, width=50 ,textvariable=productCp, font=('-family {Segoe UI} -size 12 '),background="#f7f7f7" ,border=2)
        costPrice_e.place(x=10, y=220)

        sellingPrice_l = Label(additemContainer,   text= textVariable+" selling Price", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        sellingPrice_l.place(x=10, y=260)
        sellingPrice_e = Entry(additemContainer,textvariable=productSp, width=50 , font=('-family {Segoe UI} -size 12 '),background="#f7f7f7" ,border=2)
        sellingPrice_e.place(x=10, y=300)

        def cancel():
            newProduct.destroy()
            self.product()
            
            
        def confirm():
            #getting value from entries
            name = name_e.get()
            quantity = quantity_e.get()
            costPrice = costPrice_e.get()
            sellingPrice = sellingPrice_e.get()
            supplier = supplier_e.get()

            ## validating Entry
            if(name != "" and quantity != "" and costPrice != "" and sellingPrice != ""  and supplier != "" ):
                try:
                    quantity = int(quantity)
                    costPrice = float(costPrice)
                    sellingPrice = float(sellingPrice)
                except:
                    messagebox.showinfo("Entry Error", "Please Enter Quantity , Cost Price, Selling Price with valid number")
                else:
                    ## To check if user never use zero 
                    if(quantity > 0 and costPrice > 0  and sellingPrice > 0):
                        #print(f"quantity is {quantity} cp is {costPrice} and sp {sellingPrice}")
                        if messagebox.askyesno("Confirm Field Entry", message= "Are you sure to perform this operation!" ):
                            ##To do 
                            ## Adding the product to the database
                            ##Removing the screen after adding into database
                            
                            if(state == "new"):
                                product = Product(
                                productName=name,
                                quantity=quantity,
                                cost=costPrice,
                                price=sellingPrice,
                                supplier=supplier,
                                )
                                PRODUCT.addRow(product)

                                report = Report(
                                    customer="Admin",
                                    type="Order",
                                    date = datetime.datetime.now().date(),
                                    productName = name,
                                    quantity = quantity,
                                    amount = costPrice * quantity,
                                    month=calendar.month_name[datetime.datetime.now().month]
                                )

                                REPORT.addRow(report)
                            else:
                                PRODUCT.updateRow(
                                    selectcolumn="productid",
                                    value=item[0],
                                    columns=("name", "quantity", "cost", "price", "supplier"),
                                    values=(name, quantity, costPrice, sellingPrice, supplier)
                                    )  
                               # PRODUCT.updateRow(product)
                            messagebox.showinfo("Success", "Successfully " + confirmText +" to database")

                            newProduct.destroy()
                            self.product()
                    else:
                        messagebox.showinfo("Error", "Values cannot be negative or zero")

                
            else:
                messagebox.showinfo("Error", "One or More Field is empty. Please Fill all the entries.")



            
        cancelButton = Button(additemContainer,background="RED", width = 15 ,height=2,text="Cancel",font="-family {Segoe UI} -size 10 -weight bold" , command=cancel )
        cancelButton.place(x = 750 , y =350 )
        saveButton = Button(additemContainer,background="GREEN", width = 15 ,height=2,text=confirmText,font="-family {Segoe UI} -size 10 -weight bold" , command=confirm )
        saveButton.place(x = 900 , y = 350)

    def order(self):
        self.orderContainer = tk.Frame(self.Container)
        self.orderContainer.place(x=0, y=0, height=703, width=1085)
        self.orderContainer.configure(relief="groove")
        self.orderContainer.configure(background="#c0c0c0")       
        
        addButton = Button(self.orderContainer,background="#458afc", width = 15 ,height=2,text="Add New Order",font="-family {Segoe UI} -size 10 -weight bold", command=self.addorders )
        addButton.place(x = 10 , y = 10)

        productList = Frame(self.orderContainer,height= 550, width = 1050, bg= "#f7f7f7")
        productList.place(x = 10, y = 50, )
        headingFrame = Frame(productList, background="#ffffff")
        headingFrame.place(x= 10,y= 55)
        headings = ["Bill no", "Client Name" , "Phone Number","Date Time","Product Name","Total Product","Total Amount" ]
        
        for i in range(7):
            #element = StringVar(value =headings[i])
            heading = Button(headingFrame,background="#c0c0c0", width = 17 ,height=1,text=headings[i],font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' )

           # heading= Entry(headingFrame ,width=16, fg='Black',border= 2,state='disabled',justify= 'center', textvariable=element, font="-family {Segoe UI} -size 12 -weight bold ",foreground ="Black",background="#f7f7f7")
            heading.grid(column=i , row = 0)
        TSeparator1 = ttk.Separator(productList, orient='horizontal')
        TSeparator1.place(x= 10, y = 95 ,width= 1050, height=5)
        demosales = [
            ["Bill123","David John","Client Phone", "04-01-2004","Butter","3","#15000"],
            ["Bill124","David Mike","Client Phone", "04-01-2003","Mouse","2","#4000"],
            ["Bill125","Junie carter","Client Phone", "04-01-2002","Movie","5","#24000"],
            ["Bill126","Mike wood","Client Phone", "04-01-2001","Phone","6","#12000"],
            ["Bill127","Belly herry","Client Phone", "04-01-2004","Phone","3","#15000"],
            ["Bill128","ramon widern","Client Phone", "04-01-2003","Mouse","2","#4000"],
            ["Bill129","Carry testla","Client Phone", "04-01-2002","Movie","5","#24000"],
            ["Bill130","Alberto Richard","Client Phone", "04-01-2001","Desktop","6","#12000"],
            ["Bill131","Madden tar","Client Phone", "04-01-2004","Laptop","3","#15000"],
            ["Bill132","Junie carty","Client Phone", "04-01-2003","Mouse","2","#4000"],
            ["Bill133","Fish sailor","Client Phone", "04-01-2002","Movie","5","#24000"],
            ["Bill134","akin lod","Client Phone", "04-01-2001","Lolly","6","#12000"],
            ["Bill135","Sap shoe","Client Phone", "04-01-2004","Phone","3","#15000"],
            ["Bill1136","Majeed ramon","Client Phone", "04-01-2003","Mouse","2","#4000"],
            ["Bill137","hewlet pack","Client Phone", "04-01-2002","Berry","5","#24000"],
            ["Bill138","Sam richard","Client Phone", "04-01-2001","Soda","6","#12000"],
            ["Bill139","Typing ramo","Client Phone", "04-01-2004","Cream","3","#15000"],
            ["Bill140","wish gurry","Client Phone", "04-01-2003","Mouse","2","#4000"],
            ["Bill141","jeniffar mathews","Client Phone", "04-01-2002","Snacks","5","#24000"],
            ["Bill142","typo kelly","Client Phone", "04-01-2001","Bread","6","#12000"],
            
        ]

        # allSales = ORDER.readAllrows()
        allSales = ORDER.readColumn(
            columns = ("billnumber", "clientname", "phonenumber", "date", "productname", "quantity", "amount")
        )
        global endingValue , startingValue, currentPage
        global previousButtonState ,nextButtonState
        global y
        y = 5
        startingValue = int(0)
        currentPage = int(1)
        endingValue = int(7) if len(allSales) > 7 else len(allSales)
        previousButtonState = 'disabled'
        nextButtonState = 'active'
        #startingValue = int(0)
        #endingValue = int(7)
        def showSales():
            ordersDropDown = Frame(productList,width=1050,background="#f7f7f7", height= 400)
            ordersDropDown.place(x =10 , y = 100)
            global endingValue, startingValue, currentPage
            global previousButtonState ,nextButtonState
            
            
            global y
            
            for r in range(startingValue, endingValue):                
                itemContainer = Frame(ordersDropDown, width=1050, height= 10)
                itemContainer.place(x=0,y =y)
                itemContainer.configure(relief="groove")
                backgroundColor = "#F2F2F2" if r % 2==0 else "White"
                itemContainer.configure(background= backgroundColor )
                for c in range(0, 7):
                    tableEntry = Button(itemContainer,background=backgroundColor, width = 17 ,height=2,text=allSales[r][c],font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' ,foreground="Black")
                    tableEntry.grid(column=c , row = 0)  
              
                y += 50  
            def previousButton():
                global  startingValue, endingValue , y, currentPage
                endingValue =  startingValue 
                startingValue -= 7 
                currentPage -=1
                y = 5
                ordersDropDown.pack_forget()
                showSales()
            def nextButton():
                global  startingValue, endingValue ,y, difference, currentPage
                difference = len(allSales) - endingValue
                if(difference >= 7):
                    startingValue += 7
                    endingValue +=  7
                else:
                    startingValue  = endingValue  
                    endingValue += difference
                y = 5
                currentPage +=1
                ordersDropDown.pack_forget()
                showSales()
                            
            if startingValue == 0:
                previousButtonState = 'disabled'
            else:
                previousButtonState = 'active'
            if endingValue >= len(allSales):
                nextButtonState = 'disabled'
            else:
                nextButtonState = 'active'
            previousButton = Button(productList,bg = "#f7f7f7", state=previousButtonState , text="Previous",font=('-family {Segoe UI} -size 12 -weight bold '), command=previousButton)
            previousButton.place(x =850 , y = 475 )
            currentCount = Button(productList,bg = "#f7f7f7",state='disabled', width=3,border=0, text=str(currentPage),font=('-family {Segoe UI} -size 12 -weight bold '))
            currentCount.place(x =940 , y = 480 )
            nextButton = Button(productList,bg = "#f7f7f7",state=nextButtonState , text="Next",font=('-family {Segoe UI} -size 12 -weight bold '),command= nextButton)
            nextButton.place(x =990 , y = 475 )
        showSales()


        
        
                 
    def addorders(self):
        dummyProduct = ["car","house","laptop","desktop","mouse"]
        products = [name[0] for name in PRODUCT.readColumn(('name', ))]

        self.orderContainer.destroy()
        global price, amount
        price = 0
        amount = 0

        newOrder = tk.Frame(self.Container)
        newOrder.place(x=0, y=0, height=450, width=1085)
        newOrder.configure(relief="groove")
        newOrder.configure(background="#c0c0c0")
        Label1 = Label(newOrder)
        Label1.place(x=10, y =0)
        Label1.configure (
            background="#c0c0c0",
            borderwidth="0",
            compound='left',
            disabledforeground="#a3a3a3",
            foreground="#3f3f3f",
            font="-family {Segoe UI} -size 15 -weight bold",
            text='''Add new Products''')
        addOrderContainer = Frame(newOrder,height= 600, width = 1050, bg= "#f7f7f7")
        addOrderContainer.place(x = 10, y = 50, )
        clientName_l=Label(addOrderContainer,text="Client Name",font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        clientName_l.place(x=10,y=20)
        #userbox = Entry(loginframe,width=35, font=('arial 18 bold'),bg="#F0FEF6")
        clientName_e=Entry(addOrderContainer,width=50,font=('arial 12 bold') ,background="#f7f7f7" ,border=2)
        clientName_e.place(x=10,y=60)

        clientAddress_l=Label(addOrderContainer,text="Client Address",font=('-family {Segoe UI} -size 12  ') ,background="#f7f7f7")
        clientAddress_l.place(x=10,y=100)
        clientAddress_e = Entry(addOrderContainer, width=50, font=('-family {Segoe UI} -size 12 '),background="#f7f7f7", border=2)
        clientAddress_e.place(x=10, y=140)

        phoneNumber_l = Label(addOrderContainer,  text="Client Phone number ", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        phoneNumber_l.place(x=10, y=180)
        phoneNumber_e = Entry(addOrderContainer, width=30 , font=('-family {Segoe UI} -size 12 '),background="#f7f7f7" ,border=2)
        phoneNumber_e.place(x=10, y=220)

        productName_l = Label(addOrderContainer,  text="Choose Product ", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        productName_l.place(x=10, y=260)
        ### This should be a drop down menu
        Listitem = StringVar(value = products)
        
        productName = StringVar()
       # productName.set("Choose a product")
       
        quantity_label = Label(addOrderContainer,  text="Qty ", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
        quantity_label.place(x=300, y=260)
        ### Quantity of the order
        quantity_e = Entry(addOrderContainer, width=5 , font=('-family {Segoe UI} -size 12 -weight bold '),background="#f7f7f7" ,border=2)
        quantity_e.place(x=300, y=300)
        
        def rateAmount():
            global price , amount    
            price = "" if price == 0 else price
            amount = "" if amount ==0 else amount 
            price = StringVar(value = price)
            amount = StringVar(value = amount)
            rate_e = Entry(addOrderContainer, width=10 ,textvariable=price, font=('-family {Segoe UI} -size 12 -weight bold '),background="#c0c0c0" ,border=3, state="readonly")
            rate_e.place(x=380, y=300)

            amount_label = Label(addOrderContainer,  text="Amount", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
            amount_label.place(x=500, y=260)
            ### This would be gotten from the database
            amount_e = Entry(addOrderContainer, width=15 , textvariable=amount,  font=('-family {Segoe UI} -size 12 -weight bold '),background="#c0c0c0" ,border=3, state="readonly")
            amount_e.place(x=500, y=300)
            rate_label = Label(addOrderContainer,  text="Cost Per Unit", font=('-family {Segoe UI} -size 12 '),background="#f7f7f7")
            rate_label.place(x=380, y=260)
        productName_e = ttk.Combobox(addOrderContainer,width = 30, textvariable = productName , values=products, font=('-family {Segoe UI} -size 10 '),background="#f7f7f7" )
        def productSelected(event):
            productName  = productName_e.get()
            ##TODO QUERING THE DATABASE FOR THE PRICE  

            ## using a dummy price 
            global price 
            global amount
            price = len(productName)
            price = PRODUCT.readSpecificColumn(('price', ), ('name',), (productName,) )[0][0]
            
            if productName != "" and quantity_e.get() !="":
                amount = int(quantity_e.get()) * price
            else:
                amount = 0
            rateAmount()

            #amount_e.insert(END,"hello")
            #rate_e.insert(END,"hjjs")

        rateAmount()
        productName_e.bind("<<ComboboxSelected>>", productSelected)  
        quantity_e.bind('<Return>', productSelected)
        productName_e.place(x=10, y=300)
        
        
        
        ### This would be gotten from the database
        # The text will  be equals to 0 by default 
       
       # price = StringVar(value=price)
       # amount = StringVar(value=amount)
        
        
        def cancel():
            newOrder.destroy()
            self.order()
        def confirm():
            #getting required value from entries
            clientName = clientName_e.get()
            clientAddress = clientAddress_e.get()
            phoneNumber = phoneNumber_e.get()
            productName = productName_e.get()
            quantity = quantity_e.get()
            ## This amount will be gotten from entry box
            # amount = amount_e.get()


            ## validating Entry
            if(clientName != "" and quantity != "" and clientAddress != "" and phoneNumber != "" and productName != "" ):
                try:
                    quantity = int(quantity)
                except:
                    messagebox.showinfo("Entry Error", "Please Enter Quantity with a valid number")
                else:
                    ## To check if user never use zero 
                    if(quantity > 0):
                        if messagebox.askyesno("Confirm Order", message="Are you sure to complete this order"):                            ##To do 
                            #TODO
                            ## Adding the order to the database
                            ##Removing the screen after adding into database
                            newTransactionOrder = TransactionOrder(
                                billnumber=TransactionOrder.generateBillNumber(),
                                clientname=clientName,
                                clientaddress=clientAddress,
                                phonenumber=phoneNumber,
                                date = datetime.datetime.now().strftime('%Y-%m-%d'),
                                productname=productName,
                                quantity = quantity,
                                totalamount = float(amount.get())
                            )
                            ORDER.addRow(newTransactionOrder)
                            
                            newReport = Report(
                                customer = clientName,
                                type = 'Sales',
                                date = datetime.datetime.now().date(),
                                productName = productName,
                                quantity = quantity,
                                amount = float(amount.get()),
                                month=calendar.month_name[datetime.datetime.now().month]                         
                            )

                            REPORT.addRow(newReport)
                            messagebox.showinfo("Order Succesfull", "New order has been created successfully")

                            self.order()
                            newOrder.destroy()
                            
                    else:
                        messagebox.showinfo("Error", "Quantity value cannot negative or zero")

                
            else:
                messagebox.showinfo("Error", "One or More Field is empty. Please Fill all the entries.")
                
        
           
        clearButton = Button(addOrderContainer,background="RED", width = 15 ,height=2,text="Cancel",font="-family {Segoe UI} -size 10 -weight bold" , command=cancel)
        clearButton.place(x = 750 , y =350 )
        saveButton = Button(addOrderContainer,background="GREEN", width = 15 ,height=2,text="Confirm",font="-family {Segoe UI} -size 10 -weight bold" ,command=confirm )
        saveButton.place(x = 900 , y = 350)    
        
    def report(self):
        self.reportContainer = tk.Frame(self.Container)
        self.reportContainer.place(x=0, y=0, height=703, width=1085)
        self.reportContainer.configure(relief="groove")
        self.reportContainer.configure(background="#c0c0c0")
        reportPage = Frame(self.reportContainer,background="#f7f7f7", width= 1050, height=550)
        reportPage.place(x = 10 , y = 20)
        companyLabel = Label(reportPage, background="#f7f7f7",font="-family {Segoe UI} -size 16 -weight bold" , text="DELIGHT SUPERMARKET" , foreground= "Black")
        
        companyLabel.place(x = 400, y = 10)
        companyaAddress = Label(reportPage, background="#f7f7f7",font="-family {Segoe UI} -size 13 -weight bold" , text="NO 27 BACKOFF STREET NEW WHALE ROAD" , foreground= "Black")
        companyaAddress.place(x = 330, y =40)
        companyEmail = Label(reportPage, background="#f7f7f7",font="-family {Segoe UI} -size 13 -weight bold" , text="delightsupermarket@gmail.com" , foreground= "Black")
        companyEmail.place(x= 390, y = 65)
        companyPhone = Label(reportPage, background="#f7f7f7",font="-family {Segoe UI} -size 13 -weight bold" , text="+777xxxxxxxxxx" , foreground= "Black")
        companyPhone.place(x= 450, y = 90)
        TSeparator1 = ttk.Separator(reportPage, orient='horizontal')
        TSeparator1.place(x= 0, y = 120 ,width= 1050, height=2)
        headings = ["S/N", "Customer","Type","DATE","ProductName","Total Product","Amount" ]
        demoreport = [
            ["1","Customer 1", "Order","2020-01-09","Laptop","10", "#12000"],
            ["2","Customer 2", "Sales","2020-01-05","Mone","12", "#12000"],
            ["3","Customer 3", "Order","2020-01-12","Card","15", "#15000"],
            ["4","Customer 4", "Sales","2020-01-12","Mouse","1", "#15000"],
            ["5","Customer 5", "Order","2020-01-14","Bread","14", "#62000"],
            ["6","Customer 6", "Order","2020-01-12","Cream","19", "#72000"],
            ["7","Customer 7", "Order","2020-01-23","Water","20", "#17000"],
            ["8","Customer 9", "Order","2020-01-13","Book","35", "#12700"],
            ["9","Customer 8", "Order","2020-01-12","Fan","10", "#12500"],
            ["10","Customer 1", "Order","2020-01-14","Net","12", "#11000"]
            ]
        
        allreports = REPORT.readAllrows()

        headingFrame = Frame(reportPage, background="#ffffff")
        headingFrame.place(x= 10,y= 122)
        for c in range(7):               
            tableEntry = Button(headingFrame,background="#c0c0c0", width = 17 ,height=1,text=headings[c],font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' ,foreground="Black")
            #tableEntry= Entry(itemContainer ,width=16, fg='Black',border= 2,state='disabled',justify= 'center', textvariable=element, font="-family {Segoe UI} -size 12 -weight bold ",foreground ="Black",background=backgroundColor)
            tableEntry.grid(column=c , row = 0)  
        date=datetime.datetime.now().month

        global endingValue , startingValue, currentPage
        global previousButtonState ,nextButtonState
        global y
        y = 5
        startingValue = int(0)
        currentPage = int(1)
        endingValue = int(7) if len(allreports) > 7 else len(allreports)
        previousButtonState = 'disabled'
        nextButtonState = 'active'
        
        def showReport(month = calendar.month_name[date] ,type = "all" ):
            ##TODO REPORT FROM DATABASE WILL BE FECTCHED WITH MONTH AND TYPE PARAMETER
            if type.lower() == "all":
                allreports = REPORT.readSpecificRow(('month', ), (month, ))
            else:    
                allreports = REPORT.readSpecificRow(('month', 'type'), (month, type))
            ## THE DATA WILL BE USED TO SUPPLY THE UI
            global reportDropDown                       
            global endingValue, startingValue, currentPage
            global previousButtonState ,nextButtonState
            global y
            reportDropDown = Frame(reportPage,width=1050,background="#f7f7f7", height= 400)
            reportDropDown.place(x =10 , y = 150)     
            for r in range(startingValue, endingValue):                
                itemContainer = Frame(reportDropDown, width=1050, height= 10)
                itemContainer.place(x=0,y =y)
                itemContainer.configure(relief="groove")
                backgroundColor = "#F2F2F2" if r % 2==0 else "White"
                itemContainer.configure(background= backgroundColor )
                for c in range(7):
                    tableEntry = Button(itemContainer,background=backgroundColor, width = 17 ,height=2,text=allreports[r][c],font="-family {Segoe UI} -size 10 -weight bold", state='disabled', justify='center' ,foreground="Black")
                    #tableEntry= Entry(itemContainer ,width=16, fg='Black',border= 2,state='disabled',justify= 'center', textvariable=element, font="-family {Segoe UI} -size 12 -weight bold ",foreground ="Black",background=backgroundColor)
                    tableEntry.grid(column=c , row = 0)  
               
                y += 50  
            def previousButton():
                global  startingValue, endingValue , y, currentPage
                endingValue =  startingValue 
                startingValue -= 7 
                currentPage -=1
                y = 5
                reportDropDown.pack_forget()
                showReport()
            def nextButton():
                global  startingValue, endingValue ,y, difference, currentPage
                difference = len(allreports) - endingValue
                if(difference >= 7):
                    startingValue += 7
                    endingValue +=  7
                else:
                    startingValue  = endingValue  
                    endingValue += difference
                y = 5
                currentPage +=1
                reportDropDown.pack_forget()
                showReport()
                            
            if startingValue == 0:
                previousButtonState = 'disabled'
            else:
                previousButtonState = 'active'
            if endingValue >= len(allreports):
                nextButtonState = 'disabled'
            else:
                nextButtonState = 'active'
            previousButton = Button(reportPage,bg = "#f7f7f7", state=previousButtonState , text="Previous",font=('-family {Segoe UI} -size 12 -weight bold '), command=previousButton)
            previousButton.place(x =850 , y = 510 )
            currentCount = Button(reportPage,bg = "#f7f7f7",state='disabled', width=3,border=0, text=str(currentPage),font=('-family {Segoe UI} -size 12 -weight bold '))
            currentCount.place(x =940 , y = 515 )
            nextButton = Button(reportPage,bg = "#f7f7f7",state=nextButtonState , text="Next",font=('-family {Segoe UI} -size 12 -weight bold '),command= nextButton)
            nextButton.place(x =990 , y = 510 )
            ## test amount  
            sold = "#8000"
            purchased = "#4000"
            amountPurchased = Button(reportPage,bg = "#f7f7f7",state='disabled', border=0, text="Purchased: " + purchased,font=('-family {Segoe UI} -size 12 -weight bold '))
            amountPurchased.place(x =10 , y = 515 )
           
            amountSold = Button(reportPage,bg = "#f7f7f7",state='disabled', border=0, text="Sold: " + sold,font=('-family {Segoe UI} -size 12 -weight bold '))
            amountSold.place(x =150 , y = 515 )
           
            
        showReport()
        
        months = ['January', 'February', 'March', 'April', 
                'May','June', 'July', 'August', 'September', 
                'October', 'November', 'December'] 
        options = ["All", "Order", "Sales"]
        choseMonth = StringVar()
        choseOption = StringVar()
        def changeEvent(event):
            global reportDropDown
            reportDropDown.destroy()
            global y
            y = 5                          
            showReport(month=choseMonth.get(),type= choseOption.get())           
        choseMonth.set(calendar.month_name[date])
        choseOption.set("All")
        monthLabel = Label(reportPage, background="#f7f7f7",font="-family {Segoe UI} -size 13 " , text="Month" , foreground= "Black")
        monthLabel.place(x= 700, y = 90)
        monthEntry = OptionMenu(reportPage,choseMonth,*months,command= changeEvent)
        monthEntry.place(x = 760, y = 89)
        typeLabel = Label(reportPage, background="#f7f7f7",font="-family {Segoe UI} -size 13 " , text="Type" , foreground= "Black")
        typeLabel.place(x= 870, y = 90)
        typeEntry = OptionMenu(reportPage,choseOption,*options, command= changeEvent)
        typeEntry.place(x = 920, y = 89)
            
        
    def switchTool(self, toolName, func):
        self.CurrentToolLabel.config(text=toolName)
        self.currentToolbutton.config(state=tk.NORMAL)
        self.currentToolbutton = self.toolButton[toolName]
        self.currentToolbutton.config(state=tk.DISABLED)

        for wid in self.Container.winfo_children():
            wid.destroy()

        func()

    def quit(self):        
        if messagebox.askyesno("Simple Inventory System", message="Quit Application?"):
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
