import mysql.connector as mc
from tkinter import *
from tkinter import messagebox

mydb = mc.connect(
    host="localhost",
    user="root",
    password="Apurv@2006",
    database="user_pass")
cur = mydb.cursor()
    
root = Tk()
root.title("Sign In")
def diary_window():
    def Settings():
        global co
        top1 = Toplevel()
        top1.title("Setting")
        
        FSHeader = Frame(top1)
        FSHeader.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        FInfo = LabelFrame(top1, text="INFO")
        FInfo.grid(row=1, column=0, padx=5, pady=5)
        FDelPass = LabelFrame(top1, text="SETTING")
        FDelPass.grid(row=1, column=1, padx=5, pady=5)
        
        
        cur.execute("Select * from data where username = %s", (u,))
        data = cur.fetchone()
        co = int(data[0])
        n = str(data[2])
        p = str(data[3])
        
        HeadL = Label(FSHeader, text="Setting", font=("Helvetica", 25, "bold"), padx=5, pady=5, fg="#FF4242")
        HeadL.pack()
        CodeL=Label(FInfo, text="Code: ")
        CodeL.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        NameL=Label(FInfo, text="Name: ")
        NameL.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        UserNameL=Label(FInfo, text="User: ")
        UserNameL.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        PassL=Label(FInfo, text="Pass: ")
        PassL.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        CodeE=Entry(FInfo, width = 12, bg="#FFE8E8")
        CodeE.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        CodeE.insert(0, f"{co}")
        NameE=Entry(FInfo, width=25, bg="#FFE8E8")
        NameE.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        NameE.insert(0, f"{n}")
        UserE=Entry(FInfo, width=25, bg="#FFE8E8")
        UserE.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        UserE.insert(0, f"{u}")
        PassE=Entry(FInfo, width=25, bg="#FFE8E8")
        PassE.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        PassE.insert(0, f"{p}")
        
        def delete_function():
            res = messagebox.askyesno("Delete Account", "Do You Really Want to Delete this Account\nThis Account Can Not Be Revived Later")
            if res:
                cur.execute("DELETE FROM data WHERE code = %s", (co,))
                mydb.commit()
                root.destroy()
            else:
                top1.destroy()
        def change_function():
            top2 = Toplevel()
            top2.title("Password Change")
            def change2_function():
                if p == OldPassE.get():
                    res2 = messagebox.askyesno("Password", "Do You Want to Change the Password?")
                    if res2:
                        cur.execute("UPDATE data SET password = %s WHERE code = %s", (NewPassE.get(), co))
                        mydb.commit()
                        top1.destroy()
                        top2.destroy()
                    else:
                        top1.destroy()
                else:
                    messagebox.showerror("Wrong Password", "The Old Password You Enterd Is Wrong Please Try Again")
                    top2.destroy()
            OldPassL=Label(top2, text="Old Pass: ")
            OldPassL.grid(row=0, column=0, sticky=W, padx=5, pady=5)
            NewPassL=Label(top2, text="New Pass: ")
            NewPassL.grid(row=1, column=0, sticky=W, padx=5, pady=5)
            OldPassE=Entry(top2, width=25, bg="#FFE8E8")
            OldPassE.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            NewPassE=Entry(top2, width=25, bg="#FFE8E8")
            NewPassE.grid(row=1, column=1, sticky=W, padx=5, pady=5)
            Chan = Button(top2, text="Change", command=change2_function, bg="#FAD0D0")
            Chan.grid(row=2, column=1, padx=5, pady=10, sticky=E)
            
        Del = Button(FDelPass, text="Delete", command=delete_function, padx=9, bg="#FAD0D0")
        Del.grid(row=0, column=0, padx=5, pady=5)
        Passwo = Button(FDelPass, text="Password", command=change_function, bg="#FAD0D0")
        Passwo.grid(row=1, column=0, padx=5, pady=5)
        
    top = Toplevel()
    top.title("My Diary")
    
    HelloL = Label(top, text="Hello, "+u, font=("Helvetica", 15, "bold"), fg="#FF4242")
    HelloL.place(x=5, y=15)
    Dhead1 = Frame(top)
    Dhead1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    Dlist = LabelFrame(top, text="FILE")
    Dlist.grid(row=1, column=0, padx=5, pady=5) 
    Dtext = LabelFrame(top, text="WRITING SECTION")
    Dtext.grid(row=1, column=1, padx=5, pady=5) 
    DButton = Frame(top)
    DButton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    HLabel = Label(Dhead1, text="MY DIARY", font=("Helvetica", 25, "bold"), padx=5, pady=5, fg="#FF4242")
    HLabel.grid(row=0, column=0, sticky=N)
    SetButton = Button(top, text="Setting", command=Settings, bg="#FAD0D0")
    SetButton.place(x=1030, y=22)
    
    filelist = Listbox(Dlist, height=30, width=40, bg="#FFE8E8")
    filelist.pack(padx=5, pady=5)
    def insert_list():
        filelist.delete(0, END)
        cur.execute("Select code from data where username = %s", (u,))
        c = cur.fetchone()
        co = int(c[0])
        cur.execute("Select name from notepad where code = %s", (co,))
        fetch = cur.fetchall()
        for i in range(len(fetch)):
            lfetch = list(fetch[i])
            ck = str(lfetch[0])
            filelist.insert(END, ck)
    insert_list()
    
    textbox = Text(Dtext, height=30, width=100, bg="#FFE8E8")
    textbox.pack(padx=5, pady=5)
    
    def create():
        top2=Toplevel()
        top2.title("New File")
        def create2():
            res = messagebox.askyesno("Confirm", "Do You Want To Create This File")
            cur.execute("Select code from data where username = %s", (u,))
            c = cur.fetchone()
            co = int(c[0])
            di = NewEntry.get()
            if res:
                cur.execute("INSERT INTO notepad (code, name) VALUES (%s, %s)", (co, di))
                mydb.commit()
                insert_list()
                top2.destroy()
            else:
                top2.destroy()
        NewLabel = Label(top2, text="File Name: ")
        NewLabel.grid(row=0, column=0, padx=5, pady=5)
        NewEntry = Entry(top2, width=40, bg="#FFE8E8")
        NewEntry.grid(row=0, column=1, padx=5, pady=5)
        CreBut = Button(top2, text="Create", command=create2, bg="#FAD0D0")
        CreBut.grid(row=0, column=2, padx=5, pady=5)
    addb = Button(DButton, text="ADD", command=create, bg="#FAD0D0")
    addb.grid(row=0, column=0, padx=5, pady=5)
    
    def openn():
        global ol
        ol = filelist.get(ANCHOR)
        res = messagebox.askyesno("Confirm", "Do You Want To Open This File")
        if res:
            cur.execute("Select content from notepad where name = %s", (ol, ))
            fetch = cur.fetchone()
            tfetch = list(fetch)
            strfetch = str(tfetch[0])
            textbox.delete(1.0, END)
            textbox.insert(1.0, strfetch)
            Dtext.config(text=ol)
    
    oppenb = Button(DButton, text="OPEN", command=openn, bg="#FAD0D0")
    oppenb.grid(row=0, column=1, padx=5, pady=5)
    
    def save(): # Problem: depending upon ol file
        stri = textbox.get(1.0, END)
        res = messagebox.askyesno("Confirm", "Do You Want To Save This File")
        if res:
            cur.execute("UPDATE notepad SET content=%s WHERE name=%s", (stri, ol))
            mydb.commit()
            textbox.delete(1.0, END)
            Dtext.config(text="WRITING SECTION")
            insert_list()
        
    savve = Button(DButton, text="SAVE", command=save, bg="#FAD0D0")
    savve.grid(row=0, column=3, padx=5, pady=5)
    
    def delet():
        ck = filelist.get(ANCHOR)
        res = messagebox.askyesno("Confirm", "Do You Want To Delete This File")
        if res:
            cur.execute("DELETE FROM notepad WHERE name = %s", (ck,))
            mydb.commit()
            textbox.delete(1.0, END)
            Dtext.config(text="WRITING SECTION")
            insert_list()
        
    dele = Button(DButton, text="DEL", command=delet, padx=5, bg="#FAD0D0")
    dele.grid(row=0, column=2, padx=5, pady=5)
    
    exitcc = Button(DButton, text="QUIT", command=root.destroy, bg="#FAD0D0")
    exitcc.grid(row=0, column=4, padx=5, pady=5)
def Sign_Up_Page(event):  # Problem : Can take Same Values
    top = Toplevel()
    top.title("Sign Up Area")
    def Sign_Up_Save():
        n = NameSUE.get()
        p = PasswordSUE.get()
        u = UserNameSUE.get()
        cur.execute(f"INSERT INTO data (username, name, password) VALUES (%s, %s, %s)", (u, n, p))
        mydb.commit()
        messagebox.showinfo("Congrats", "Your Account is Made Successfully")
        top.destroy()
        
    frame4 = Frame(top)
    frame4.pack()
    frame5 = Frame(top)
    frame5.pack()
    SignUpL = Label(frame4, text="Sign Up", font=("Helvetica", 25, "bold"), padx=5, pady=5, fg="#FF4242")
    SignUpL.pack()
    
    NameSUL = Label(frame5, text="Full Name: ")
    NameSUL.grid(row= 0, column=0, padx=15, pady=5)
    UserNameSUL = Label(frame5, text="User Name: ")
    UserNameSUL.grid(row= 1, column=0, pady=5)
    PasswordSUL = Label(frame5, text="Password: ")
    PasswordSUL.grid(row= 2, column=0, padx=15, pady=5)
    
    NameSUE = Entry(frame5, width=25, bg="#FFE8E8")
    NameSUE.grid(row= 0, column=1, padx=15, pady=5)
    UserNameSUE = Entry(frame5, width=25, bg="#FFE8E8")
    UserNameSUE.grid(row= 1, column=1, padx=15,  pady=5)
    
    PasswordSUE = Entry(frame5, width=25, bg="#FFE8E8")
    PasswordSUE.grid(row= 2, column=1, padx=15,  pady=5)
    
    
    Save = Button(frame5, text="Sign Up", command=Sign_Up_Save, bg="#FAD0D0")
    Save.grid(row=3, column=0, columnspan=2, padx=15, pady=10, sticky=SE)
def Sign_In_Function():  # Problem : Sign In Function Random Values from different schema Correct
    global u
    Un=UserEntSI.get()
    u = UserEntSI.get()
    Pass=PassEntSI.get()
    Untru=False
    PassChe=False
    
    cur.execute("Select username from data")
    Untup=cur.fetchall()
    for i in range(len(Untup)):
        a = list(Untup[i])
        b = str(a[0])
        if Un == b:
            Untru=True
            
    cur.execute("Select password from data")
    Passtup=cur.fetchall()
    
    for i in range(len(Passtup)):
        a = list(Passtup[i])
        b = str(a[0])
        if Pass == b:
            PassChe=True
            
    if Untru and PassChe:
        UserEntSI.delete(0, END)
        PassEntSI.delete(0, END)
        diary_window()
    elif not PassChe and not Untru:
        messagebox.showwarning("Wrong", "You are entering wrong username & password")
        PassEntSI.delete(0, END)
        UserEntSI.delete(0, END)
    else:
        if not PassChe:
            messagebox.showwarning("Password Wrong", "Your Password is Wrong Please Check it again")
            PassEntSI.delete(0, END)
        if not Untru:
            messagebox.showwarning("Username Wrong", "Your Username is Wrong Please Check it again")
            UserEntSI.delete(0, END)


# Frames for the Sign in page
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()

# Sign in Header & Sign Up Link
Label1= Label(frame1, text="Sign In", font=("Helvetica", 25, "bold"), padx=5, pady=5, fg="#FF4242")
Label1.pack()
SingUpL = Label(frame3, text="Not A Member Wanna Sign Up? Click Here!", fg="blue", cursor="hand2")
SingUpL.pack()
SingUpL.bind("<Button-1>", Sign_Up_Page)

# Entry Boxes for Sign In Page
UserSIL = Label(frame2, text="Username: ")
UserSIL.grid(row=0, column=0, padx=15, pady=5)
PassSIL = Label(frame2, text="Password: ")
PassSIL.grid(row=1, column=0, padx=15, pady=5)
UserEntSI = Entry(frame2, width=25, bg="#FFE8E8")
UserEntSI.grid(row=0, column=1, padx=15, pady=5)
PassEntSI = Entry(frame2, show="*", width=25, bg="#FFE8E8")
PassEntSI.grid(row=1, column=1,padx=15, pady=5)
SignIn = Button(frame2, text="Sign In", command=Sign_In_Function, bg="#FAD0D0")
SignIn.grid(row=2, column=0, columnspan=2, padx=15, pady=10, sticky=SE)

root.mainloop()