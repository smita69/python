class programmer:
    def detail(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
        self.mobileno=int(input("enter your mobile no"))
        self.address=input("enter your address")
        self.course=input("enter your graduation")
    def display(self):
        print("\ndisplaying the biodata\n")
        print("name =",self.name)
        print("age =",self.age)
        print("mobile number=",self.mobileno)
        print("address=",self.address)
        print("graduation =",self.course)
p=programmer()
p.detail()
p.display()
