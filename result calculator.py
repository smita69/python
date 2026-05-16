class result:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def marksheet(self):
        n=int(input("enter the number of subjects you have"))
        self.sub_name=[]
        self.marks=[]
        for j in range(n):
            name=input("enter the name of subject")
            self.sub_name.append(name)
        for i in range(n):
            marks=int(input(f"enter marks of {self.sub_name[i]} th subject"))
            self.marks.append(marks)
        self.avg_marks=sum(self.marks)/n
        self.percentage=round((sum(self.marks)/(n*100)) *100)
    def display(self):
        for a,b in zip(self.sub_name,self.marks):
            print(f"the result  are {a} :- {b}")
        print(f"the average marks of  {self.name} is {self.avg_marks}")
        print(f"the percentage of {self.name} is {self.percentage} %")
r=result("smita","MCA")
r.marksheet()
r.display()
