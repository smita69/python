class expense:
    print("Welcome to expense traker\n------------------------------")
    def __init__(self):
        self.expenses=[]
    def user_input(self):
        name=input("enter the name of expense")
        ammount=int(input("enter the ammount of expense"))
        self.expenses.append([name,ammount])
    def display(self):
        print("-------------\n view expense\n-------------\n")
        if len(self.expenses)==0:
            print("you dont any expense")
        else:
            print("sno. \t expense \t Ammount ")
            
            
            for i,expense  in enumerate(self.expenses,start=1):
                print(f"{i}\t {expense[0]}\t \t {expense[1]} ")
    def remove(self):
        self.n=input("enter the name of expense you want to remove")
        for expense in self.expenses:
            if self.n==expense[0]:
                self.expenses.remove(expense)
                print("given expense is removed")
            else:
                print("expense is not found")
    def total(self):
        self.total=0
        for i in self.expenses:
            self.total+=i[1]
        print("The total ammount you have to pay is ",self.total)
    def exit(self):
        print("thankyou for using expense traker program")
        
obj=expense()
while True:
    print("1 for add expense")
    print("-------------------")
    print("2 for view expense")
    print("-------------------")
    print("3 for remove expense")
    print("---------------------")
    print("4 for total expense")
    print("--------------------")
    print("5 for exit expense")
    print("--------------------")
    choice=int(input("enter your choice"))
    
    if choice==1:
        obj.user_input()
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.remove()
    elif choice==4:
        obj.total()
    elif choice==5:
        obj.exit()
    else:
        print("Invalid choice")
    






            
