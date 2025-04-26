import sys
task=[]
file1=open("todo.txt","a")
completed_task=[]
def add():
    query=int(input("How many task you wanna add?"))
    file1.write("Added task:\n")
    for x in range(query):
        text=input(f"enter task {x+1}:\n")
        task.append(text)
    file1.writelines(f"{task}\n")
def mark():
    query=int(input("Which task number have you completed??"))
    for idx, t in enumerate(task):
        print(f"{idx}. {t}")
    if 0 <= query < len(task):
        completed_task.append(task[query])
        task.pop(query)
    else:
        print("Invalid task number!")
    file1.write("Completed task:\n")
    file1.writelines(f"{completed_task}\n")
def delete():
    query=int(input("Which task number you wanna delete??"))
    for idx, t in enumerate(task):
        print(f"{idx}. {t}")
    if 0 <= query < len(task):
        task.pop(query)
    else:
        print("Invalid task number!")
def pending():
    print(task)
    file1.write("Pending task:\n")
    file1.writelines(f"{task}\n")
def completed():
    print(completed_task)
def options():
    print("1.Add a task")
    print("2.Mark a task as completed")
    print("3. Delete a task")
    print("4.View pending and completed tasks")
    print("5. Exit")
while True:
    options()
    choice=int(input("Enter the options:"))
    try:
        match int (choice):
            case 1:
                add()
            case 2:
                mark()
            case 3:
                delete()
            case 4:
                choose=int(input("View pending(0) or completed(1) task(0 or 1)?"))
                if (choose==0):
                    pending()
                elif (choose==1):
                    completed()
                else:
                    print("Choose either 0 or 1")
            case 5:
                sys.exit()
    except ValueError:
        print("Please enter numbers only!")
