import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="Apurv@2006",
    database="todolist"
)
print("Your database server is connected successfully\n")

cur = mydb.cursor()  # Code Execution

while True:
    inp = input("Enter the command: ")

    if inp == "help":
        print("""AddT = Add the Task
AddP = Add the Project
VAT = View all the Task
VAP = View all the Project
VATP = View all the tasks in Project
Mark = Mark the Task Completed
DT = Delete the Task
DCT = Delete all the Completed Task
DP = Delete the Project
Exit = Exit the Program
                    """)

    elif inp == "AddT":
        task_name = input("Enter the Task Name: ")
        project_id = int(input("Enter the Project Code: "))
        cur.execute("INSERT INTO tasks (Name, Project_ID) VALUES (%s, %s);", (task_name, project_id))
        mydb.commit()  # Commit the transaction
        print("Task added successfully")

    elif inp == "AddP":
        project_name = input("Enter the Project Name: ")
        project_id = int(input("Enter the Project Code: "))
        cur.execute("insert into project (ProjectCode, ProjectName) Values (%s, %s);", (project_id, project_name))
        mydb.commit()  # Commit the transaction
        print("Project added successfully")

    elif inp == "VAT":
        cur.execute("select * from tasks where Completed = 0")
        print("All the Task View")
        result = cur.fetchall()
        for row in result:
            print(row)

    elif inp == "VAP":
        cur.execute("select * from project")
        print("All the Projects View")
        result = cur.fetchall()
        for row in result:
            print(row)

    elif inp == "VATP":
        ProjID = int(input("Enter the Project ID You want to see the task of: "))
        cur.execute("select * from tasks where Project_ID = %s and Completed = 0;", (ProjID,))
        print(f"All the Task from the {ProjID}")
        result = cur.fetchall()
        for row in result:
            print(row)

    elif inp == "Mark":
        cur.execute("select * from tasks where Completed = 0")
        print("All the Task View")
        result = cur.fetchall()
        for row in result:
            print(row)
        TaskID = int(input("Enter the Task ID You want to mark: "))
        cur.execute("Update tasks set Completed = 1 where TaskID = %s", (TaskID,))
        mydb.commit()
        print("Yeah You completed a task, Bravo!")

    elif inp == "DT":
        cur.execute("select * from tasks where Completed = 0")
        print("All the Task View")
        result = cur.fetchall()
        for row in result:
            print(row)
        TaskID = int(input("Enter the Task ID You want to Delete: "))
        cur.execute("DELETE FROM tasks WHERE TaskID = %s;", (TaskID,))
        mydb.commit()
        print(f"You deleted the TaskID:{TaskID}")

    elif inp == "DP":
        cur.execute("select * from project")
        print("All the Project View")
        result = cur.fetchall()
        for row in result:
            print(row)
        ProID = int(input("Enter the Project Code You want to Delete: "))
        cur.execute("DELETE FROM project WHERE ProjectCode = %s;", (ProID,))
        mydb.commit()
        print(f"You deleted the ProjectCode:{ProID}")

    elif inp == "DCT":
        cur.execute("delete from tasks where Completed = 1")
        mydb.commit()
        print("All the task that are completed is deleted successfully")

    elif inp == "Exit":
        break

    else:
        print("Bagadbam")
