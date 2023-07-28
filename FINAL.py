# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:37:34 2022

@author: HP
"""

from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def system():
    root = Tk()
    root.geometry("1700x900")
    root.title("Bakery Management System")

    ############database###########
    def Database():
        global conn, cursor
        # creating system database
        conn = sqlite3.connect("Bakery.db")
        cursor = conn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS RECORDS(ordno text, bre text ,mi text,cc text,bc text,ice text, co text, bro text, ct text,sb text,tax text,sr text,tot text)")

    # variable datatype assignment
    orderno = StringVar()
    bread = StringVar()
    milkshake = StringVar()
    choc_cupcake = StringVar()
    blue_cupcake = StringVar()
    icecream = StringVar()
    coffee = StringVar()
    brownie=StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        order = (orderno.get())
        bre = (float(bread.get()))
        mi = float(milkshake.get())
        cc = float(choc_cupcake.get())
        bc = float(blue_cupcake.get())
        ice = float(icecream.get())
        co = float(coffee.get())
        bro=float(brownie.get())

        # computing cost of items
        costbr = bre * 60
        costmi = mi * 50
        costcc = cc * 100
        costbc = bc * 80
        costice = ice * 100
        costco = co * 30
        costbro = bro*120

        # computing the charges
        costofmeal = (costbr + costmi + costcc + costbc + costice + costco + costbro)
        ptax = ( (costbr + costmi + costcc + costbc + costice + costco + costbro)* 0.18)
        sub = (costbr + costmi + costcc + costbc + costice + costco + costbro)
        ser = ((costbr + costmi + costcc + costbc + costice + costco + costbro) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)

        # Displaying values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)
        

    def reset():
        orderno.set("")
        bread.set("")
        milkshake.set("")
        choc_cupcake.set("")
        blue_cupcake.set("")
        icecream.set("")
        coffee.set("")
        brownie.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=900, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    # rightframe
    rightframe = Frame(root, width=400, height=700, relief=SUNKEN)
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM RECORDS")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

   
    # add some style
    style = ttk.Style()
    style.theme_use("classic")

    style.configure("Treeview",
                    background="#ffd699",
                    foregroung="black",
                    rowheight=30,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', '#e67f30')])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "bre", "mi", "cc", "bc", "ice", "co","bro", "ct", "sb", "tax", "sr", "tot")
    ############ creating  for table ################
    hsb = ttk.Scrollbar(rightframe, orient="horizontal")
    hsb.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    vsb = ttk.Scrollbar(rightframe, orient="vertical")
    vsb.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)
    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("bre", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("mi", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("cc", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("bc", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("co", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("bro", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)
    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("bre", text="Bread", anchor=CENTER)
    my_tree.heading("mi", text="Milkshake", anchor=CENTER)
    my_tree.heading("cc", text="Choc_cupcake", anchor=CENTER)
    my_tree.heading("bc", text="Blue_cupcake", anchor=CENTER)
    my_tree.heading("ice", text="Ice cream", anchor=CENTER)
    my_tree.heading("co", text="Coffee", anchor=CENTER)
    my_tree.heading("bro", text="Brownie", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    def add():
        Database()
        
        ord1 = orderno.get()
        bread1 = bread.get()
        milkshake1 = milkshake.get()
        choc_cupcake1 = choc_cupcake.get()
        blue_cupcake1 = blue_cupcake.get()
        ice1 = icecream.get()
        coffee1 = coffee.get()
        brownie1=brownie.get()
        cost1 = cost.get()
        subtotal1 = subtotal.get()
        tax1 = tax.get()
        service1 = service.get()
        total1 = total.get()
        if ord1 == "" or bread1 == "" or milkshake1 == "" or choc_cupcake1 == "" or blue_cupcake1 == "" or ice1 == "" or coffee1 == "" or brownie1 == "" or cost1 == "" or subtotal1 == "" or tax1 == "" or service1 == "" or total1 == "":
            messagebox.showinfo("Warning", "fill the empty field!!!")
        else:
            conn.execute('INSERT INTO RECORDS(ordno, bre, mi, cc ,bc, ice ,co, bro ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (ord1, bread1, milkshake1, choc_cupcake1, blue_cupcake1, ice1, coffee1, brownie1, cost1, subtotal1, tax1, service1, total1));
            conn.commit();
            messagebox.showinfo("Message", "Stored successfully")
       
        DisplayData()
        conn.close()

   #access data from sqlite
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM RECORDS")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = conn.execute("DELETE FROM RECORDS WHERE ordno= %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


    localtime = time.asctime(time.localtime(time.time()))
  
    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Bakery Management System", fg="blue", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=0)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=0)


    # items
    ordlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Order No.", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=orderno).grid(row=1, column=1)
    # bread
    brlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Bread", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)
    brtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                  textvariable=bread).grid(row=2, column=1)
    # milkshake
    milbl = Label(leftframe, font=('aria', 16, 'bold'), text="Milkshake", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)
    mitxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=milkshake).grid(row=3, column=1)
    # chocolate cupcake
    cclbl = Label(leftframe, font=('aria', 16, 'bold'), text="Chocolate cupcake", fg="black", bd=10, anchor=W).grid(row=4,
                                                                                                          column=0)
    cctxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=choc_cupcake).grid(row=4, column=1)
    # blueberry cupcake
    bclbl = Label(leftframe, font=('aria', 16, 'bold'), text="Blueberry cupcake", fg="black", bd=10, anchor=W).grid(row=5,
                                                                                                           column=0)
    bctxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=blue_cupcake).grid(row=5, column=1)
    # icecream
    icelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Ice Cream", fg="black", bd=10, anchor=W).grid(row=6,
                                                                                                             column=0)
    icetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=icecream).grid(row=6, column=1)
    # coffee
    coffeelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Coffee", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                            column=2)
    coffeetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                     textvariable=coffee).grid(row=1, column=3)
    #brownie
    brownielbl = Label(leftframe, font=('aria', 16, 'bold'), text="Brownie", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                            column=2)
    brownietxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                     textvariable=brownie).grid(row=2, column=3)
    # cost
    costlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Cost", fg="blue", bd=10, anchor=W).grid(row=3, column=2)
    costtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                    textvariable=cost).grid(row=3, column=3)
    # subtotal
    sublbl = Label(leftframe, font=('aria', 16, 'bold'), text="Subtotal", fg="blue", bd=10, anchor=W).grid(row=4,
                                                                                                           column=2)
    subtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=subtotal).grid(row=4, column=3)
    # tax
    taxlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Tax", fg="blue", bd=10, anchor=W).grid(row=5, column=2)
    taxtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                   textvariable=tax).grid(row=5, column=3)
    # service
    servicelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Service", fg="blue", bd=10, anchor=W).grid(row=6,
                                                                                                              column=2)
    servicetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                       textvariable=service).grid(row=6, column=3)
    # total
    totallbl = Label(leftframe, font=('aria', 16, 'bold'), text="Total", fg="blue", bd=10, anchor=W).grid(row=7,
                                                                                                          column=2)
    totaltxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right',
                     textvariable=total).grid(row=7, column=3)
    # ---button--

    # totalbutton
    totbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Total", bg="pink", fg="black", bd=10, padx=5, pady=5,
                    width=10, command=tottal).grid(row=8, column=1)
    # resetbutton
    resetbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Reset", bg="pink", fg="black", bd=10, padx=5,
                      pady=5, width=10, command=reset).grid(row=8, column=2)
    # exitbutton
    exitbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Exit", bg="pink", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=8, column=3)
    # Add  recordbutton
    addbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Add", bg="pink", fg="black", bd=10, padx=5, pady=5,
                    width=10, command=add).grid(row=10, column=0)
    # Deleterecordbutton
    deletebtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Delete Record", bg="pink", fg="black", bd=10,
                       padx=5, pady=5, width=10, command=Delete).grid(row=10, column=3)

 

    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Feedback form")
        conn = sqlite3.connect("Bakery.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
      
        name = StringVar()
        email = StringVar()
        comments = StringVar()

        # defining submit 
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = sqlite3.connect("Bakery.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        # defining cancel 
        def cancel():
            feed.destroy()

        # label#
        lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
        lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                     fg="black").pack(side=TOP)
        # name
        namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        # email
        emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=280, y=150)
        emailtxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=email).place(x=285, y=185)
        ###checkbutton
        ratelbl = Label(feed, font=('vardana', 15), text="How would you rate us?", fg="black", bd=10, anchor=W).place(
            x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('vardana', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('vardana', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=265)
        c3 = Checkbutton(feed, font=('vardana', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=265)
        c4 = Checkbutton(feed, font=('vardana', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=265)
        # comments"
        commentslbl = Label(feed, font=('vardana', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("vardana", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(feed, font=("vardana", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(
            x=245, y=430)
        feed.mainloop()

    # Feedbackbutton
    feedbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Feedback", fg="black", bg="cyan", bd=10, padx=5,
                     pady=5, width=10, command=feedbackk).grid(row=10, column=1)
    
    def employees():
        emp = Tk()
        emp.geometry("600x500")
        emp.title("Employee")
        conn = sqlite3.connect("Bakery.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE(n text , empid text ,sal text)")
      
        name = StringVar()
        eid = StringVar()
        salary= StringVar()

        # entering new employee 
        def submit():
            n = name.get()
            empid = eid.get()
            sal=salary.get()
            conn = sqlite3.connect("Bakery.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO EMPLOYEE VALUES ('" + n + "','" + empid + "','" + sal + "'  )")
            messagebox.showinfo("message", "data inserted !")
            emp.destroy()
            
        def cancel():
            emp.destroy()
        
        
        # label#
        lb1 = Label(emp, font=("Calisto MT", 15, "bold"), text="New employee", fg="black").pack(side=TOP)
       
        # name
        namelbl = Label(emp, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(emp, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        # email
        eidlbl = Label(emp, font=('vardana', 15), text="Employee ID:-", fg="black", bd=10, anchor=W).place(x=280, y=150)
        eidtxt = Entry(emp, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=eid).place(x=285, y=185)
        
        # comments"
        salarylbl = Label(emp, font=('vardana', 15), text="Salary", fg="black", bd=10, anchor=W).place(x=10, y=300)
        salarytxt=  Entry(emp, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=salary).place(x=15, y=335)
        
        
        
        # button
        submit= Button(emp, font=("vardana", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(emp, font=("vardana", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(
            x=245, y=430)
        emp.mainloop()

         # Employee button
    empbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Employee", fg="black", bg="cyan", bd=10, padx=5,
                     pady=5, width=10, command=employees).grid(row=10, column=2)

   #menu
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x400")
        lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Times New Roman", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblbread = Label(roott, font=("Times New Roman", 20, "bold"), text=" Bread", fg="#e67f30", bd=10)
        lblbread.grid(row=1, column=0)
        lblpriceb = Label(roott, font=("Times New Roman", 20, "bold"), text="50/-", fg="blue", bd=10)
        lblpriceb.grid(row=1, column=3)
        lblmilk = Label(roott, font=("Times New Roman", 20, "bold"), text="Milkshake", fg="#e67f30", bd=10)
        lblmilk.grid(row=2, column=0)
        lblpricem = Label(roott, font=("Times New Roman", 20, "bold"), text="50/-", fg="blue", bd=10)
        lblpricem.grid(row=2, column=3)
        lblchoc = Label(roott, font=("Times New Roman", 20, "bold"), text="Chocolate Cupcake", fg="#e67f30", bd=10)
        lblchoc.grid(row=3, column=0)
        lblpricecc = Label(roott, font=("Times New Roman", 20, "bold"), text="60/-", fg="blue", bd=10)
        lblpricecc.grid(row=3, column=3)
        lblblue = Label(roott, font=("Times New Roman", 20, "bold"), text="Blueberry Cupcake", fg="#e67f30", bd=10)
        lblblue.grid(row=4, column=0)
        lblpricebc = Label(roott, font=("Times New Roman", 20, "bold"), text="60/-", fg="blue", bd=10)
        lblpricebc.grid(row=4, column=3)
        lblicecream = Label(roott, font=("Times New Roman", 20, "bold"), text="Ice-Cream", fg="#e67f30", bd=10)
        lblicecream.grid(row=5, column=0)
        lblpricei = Label(roott, font=("Times New Roman", 20, "bold"), text="100/-", fg="blue", bd=10)
        lblpricei.grid(row=5, column=3)
        lblcoffee = Label(roott, font=("Times New Roman", 20, "bold"), text="Coffee", fg="#e67f30", bd=10)
        lblcoffee.grid(row=6, column=0)
        lblpricecof = Label(roott, font=("Times New Roman", 20, "bold"), text="30/-", fg="blue", bd=10)
        lblpricecof.grid(row=6, column=3)
        lblbrownie = Label(roott, font=("Times New Roman", 20, "bold"), text="Brownie", fg="#e67f30", bd=10)
        lblbrownie.grid(row=7, column=0)
        lblpricebro = Label(roott, font=("Times New Roman", 20, "bold"), text="100/-", fg="blue", bd=10)
        lblpricebro.grid(row=7, column=3)
        
        roott.mainloop()
    # menubutton
    menubtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Menu", bg="pink", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=menu).grid(row=8, column=0)
    root.mainloop()
system()