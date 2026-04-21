print("---------------------------TO-DO-LIST--------------------------------------------")
tasks=[]
count=int(input("enter how much task will be taken"))
for i in range(1,count+1):
    task=input("enter the task")
    tasks.append(task)
while True:

    print("choose operation that you want to perform on our tasks (1 for add task/2 for delete task/3 update task /4 for view/5 for exit)")
    choice=int(input("enter the operation(must be from given numbers it only contain digit that is given before operation name)"))
    if choice==1:
        print("you choose for addition")
        task1=input("add task")
        tasks.append(task1)
        print(f"The task is added {task1}")
    elif choice==2:
        print("you choose for detelte task")
        task2=input("enter the task that you want to delete")
        if task2 in tasks:
            ind=tasks.index(task2)
            del tasks[ind]
        else:
            print(f"{task2} is not define")
    elif choice==3:
        print("you choose for update the taks")
        task3=input("enter the task you want to update")
        if task3 in tasks:
            updated_val=input("enter the new task")
            ind2=tasks.index(task3)
            tasks[ind2]=updated_val
        else:
            print(f"{task3} is not define")
    elif choice==4:
        print("you choose for view all tasks")
        print(f"total tasks={tasks}")
    elif choice==5:
        print("you choose for exit or close the app")
        break
print(tasks)
