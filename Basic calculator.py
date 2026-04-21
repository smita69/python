print("------------------------BASIC CALCULATOR----------------------------------------")
def add():
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    sum=num1+num2
    print(sum)
def sub():
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    subs=num1-num2
    print(subs)
def multi():
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    multiply=num1*num2
    print(multiply)
def div():
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    div=num1/num2
    print(div)
def mod():
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    modulus=num2%num1
    print(modulus)
while True:
    print("choose opeation what do you want to print(1 for addition / 2 for substraction / 3 for multiplication / 4 for devision /5 for modulus /6 for exit")
    choice=int(input("your choice in digit mentioned before operation"))
    if choice==1:
        print("you choose for addition")
        add()
    elif choice==2:
        print("you choose for substraction")
        sub()
    elif choice==3:
        print("you choose for multiplication")
        multi()
    elif choice==4:
        print("you choose for division")
        div()
    elif choice==5:
        print("you choose for modulus ")
        mod()
    elif choice==6:
        print("are you sure to exit")
        ch=input("enter (ok/cancel)")
        if ch=="ok":
            break
    else:
        print("choose an operation")



