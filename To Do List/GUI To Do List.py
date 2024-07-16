from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="Apurv@2006",
    database="todolistgui"
)
cur = mydb.cursor()

root = Tk()
root.title("To-Do")

def add(event=None):
    def save(event=None):
        res = messagebox.askyesno("Save", "Do you want to save this task?")
        if res == 1:
            task_name = ent.get()
            date = cal.get()
            cur.execute("INSERT INTO task (Name, Deadline) VALUES (%s, %s);", (task_name, date))
            mydb.commit()
            top.destroy()
        else:
            top.destroy()

    def clear(event=None):
        ent.delete(0, END)
        
    def destroy(event=None):
        top.destroy()

    top = Toplevel()
    top.title("Add Task")
    top.grab_set()  # Make the window modal
    top.focus_set()  # Set focus to the new window

    Label(top, text="Enter the Task:").grid(row=0, column=0, padx=10, sticky="w")
    Label(top, text="Deadline:").grid(row=1, column=0, padx=10, sticky="w")

    ent = Entry(top, width=40)
    ent.grid(row=0, column=1, padx=10, pady=5, columnspan=3, sticky="w")
    ent.focus_set()

    cal = DateEntry(top, date_pattern="yyyy-mm-dd")
    cal.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    but1 = Button(top, text="Save", command=save, width=10, bg="#FE8572")
    but1.grid(row=2, column=1, padx=5, pady=10)
    but1.bind('<Return>', save)
    but2 = Button(top, text="Clear", command=clear, width=10, bg="#72FCFE")
    but2.grid(row=2, column=2, padx=5, pady=10)
    but2.bind('<Return>', clear)
    but3 = Button(top, text="Quit", command=destroy, width=10, bg="#72FE90")
    but3.grid(row=2, column=3, padx=5, pady=10)
    but3.bind('<Return>', destroy)
    root.wait_window(top)


def view(event=None):
    def set_anchor(event):
        global selected_index
        selected_index = list1.curselection()
        print(selected_index)
    
    def delete(event=None):
        global selected_index
        res = messagebox.askyesno("Delete", "Do want to delete this task?")
        if res == 1:
            for i in range(len(selected_index)):
                list1.selection_anchor(selected_index[i])
                task_name = list1.get(ANCHOR)
                cur.execute("DELETE FROM task WHERE Name = %s;", (task_name,))
                mydb.commit()
                list1.delete(ANCHOR)
            top.destroy()
            
    def complete(event=None):
        global selected_index
        messagebox.showinfo("Message", "Bravo You completed your task!")
        for i in range(len(selected_index)):
            list1.selection_anchor(selected_index[i])
            Name = list1.get(ANCHOR)
            cur.execute("Update task set Completed = 1 where Name = %s", (Name,))
            cur.execute("DELETE FROM task WHERE Name = %s;", (Name,))
            mydb.commit()
            list1.delete(ANCHOR)
        top.destroy()
        
    top = Toplevel()
    top.title("View all the Task")
    top.grab_set()  # Make the window modal
    top.focus_set()  # Set focus to the new window
    list1 = Listbox(top, height=20, width=35, selectmode=EXTENDED)
    list1.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
    list1.bind("<Return>", set_anchor)
    list1.bind('<Button-1>', set_anchor)
    cur.execute("select Name from task where Completed = 0")
    result = cur.fetchall()
    for row in result:
        list1.insert(END, row[0])
    
    but1 = Button(top, text="Delete", command=delete, pady=60, bg="#E64F4F")
    but1.grid(row=0, column=1, padx=5, pady=5)
    but1.bind('<Return>', delete)
    but2 = Button(top, text="Mark", command=complete, pady=60, padx=4, bg="#4FE654")
    but2.grid(row=1, column=1, padx=5, pady=5)
    but2.bind('<Return>', complete)
    root.wait_window(top)
    
fra = LabelFrame(root, text="COMMANDS", padx=5, pady=5)
fra.pack(padx=5, pady=5)

but1 = Button(fra, text="Add the Task", command=add, padx=49, bg="#82FC98")
but1.grid(row=0, column=0, padx=5, pady=5)
but1.bind('<Return>', add)

but2 = Button(fra, text="View all the Task", command=view, padx=40, bg="#FC8482")
but2.grid(row=1, column=0, padx=5, pady=5)
but2.bind('<Return>', view)


root.mainloop()