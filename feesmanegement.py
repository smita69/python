# Fees Management System using Class and Object in Python

class FeesManagement:

    def input_data(self):
        self.roll_no = int(input("Enter Roll Number : "))
        self.name = input("Enter Student Name : ")

        self.jan = float(input("January Fees : "))
        self.feb = float(input("February Fees : "))
        self.mar = float(input("March Fees : "))
        self.apr = float(input("April Fees : "))
        self.may = float(input("May Fees : "))
        self.jun = float(input("June Fees : "))
        self.jul = float(input("July Fees : "))
        self.aug = float(input("August Fees : "))
        self.sep = float(input("September Fees : "))
        self.oct = float(input("October Fees : "))
        self.nov = float(input("November Fees : "))
        self.dec = float(input("December Fees : "))

        self.bus_fee = float(input("Bus Fees : "))
        self.exam_fee = float(input("Exam Fees : "))
        self.library_fee = float(input("Library Fees : "))

    def calculate_total(self):
        self.total = (
            self.jan + self.feb + self.mar + self.apr +
            self.may + self.jun + self.jul + self.aug +
            self.sep + self.oct + self.nov + self.dec +
            self.bus_fee + self.exam_fee + self.library_fee
        )

    def display(self):
        print("\n========== FEES RECEIPT ==========")
        print("Roll Number :", self.roll_no)
        print("Student Name:", self.name)

        print("\n--- Monthly Fees ---")
        print("January   :", self.jan)
        print("February  :", self.feb)
        print("March     :", self.mar)
        print("April     :", self.apr)
        print("May       :", self.may)
        print("June      :", self.jun)
        print("July      :", self.jul)
        print("August    :", self.aug)
        print("September :", self.sep)
        print("October   :", self.oct)
        print("November  :", self.nov)
        print("December  :", self.dec)

        print("\nBus Fees      :", self.bus_fee)
        print("Exam Fees     :", self.exam_fee)
        print("Library Fees  :", self.library_fee)

        print("\nTotal Fees :", self.total)


# Object Creation
obj = FeesManagement()

# Function Calling
obj.input_data()
obj.calculate_total()
obj.display()
