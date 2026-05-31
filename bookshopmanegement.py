class book_shop:
    print("-------------------\nwelcome to this library program\n--------------------------\n")
    def __init__(self):
        self.book=[]
        self.n=input("enter the name of shop")
        self.m=int(input("enter the mobileno"))
        
    def user_input(self):
        name=input("enter the name of book")
        ammount=int(input("enter the ammount of book"))
        self.book.append([name,ammount])
        print("the book is successfully added")
    def display(self):
        if len(self.book)==0:
            print("stock is empty")
        else:
            print("------------------------\ndisplaying the available books and their price\n----------------")
            print("sno\t book\t  price\t")
            for i,books in enumerate(self.book,start=1):
                print(f"{i}\t {books[0]}\t\t{books[1]}")
    def remove(self):
        name=input("enter the name of book you want to remove")
        for book in self.book:
            if book[0]==name:
                self.book.remove(book)
                print("given book is removed")
            else:
                print("given book is not found")
    def total_expense(self):
        self.total=0
        for i in self.book:
            self.total+=i[1]
        self.gst=self.total*0.18
        self.grnd_total=self.total+self.gst
        print(f"Total expense you have spend for buying stock is {self.total}")
    def viewing_bill(self):
        print("------------------\nprinting bill\n-------------------------------\n")
        
        print(f"Name of Shop :\t\t {self.n}")
        print(f"Mobile no :\t\t {self.m}")
        print(f"Total ammount :\t\t {self.total}")
        print(f"gst :\t\t\t {self.gst}")
        print(f"Total payabel ammount :\t {self.grnd_total}")
    
    def exit(self):
        print("Thankyou for using library program")
obj=book_shop()
while True:
    print("1 for add book")
    print("2 for all  book")
    print("3 for remove book")
    print("4 for viewing total expense")
    print("5 for viewing bill")
    print("6 for exit")
    ch=int(input("enter your choice"))
    if ch==1:
        obj.user_input()
    elif ch==2:
        obj.display()
    elif ch==3:
        obj.remove()
    elif ch==4:
        obj.total_expense()
    elif ch==5:
        obj.viewing_bill()
    elif ch==6:
        obj.exit()
