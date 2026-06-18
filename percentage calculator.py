from tkinter import *
top=Tk()
top.title("percentage calculator")
top.geometry("500x300")
top.config(bg="aqua")
def calculate():
    t=total_marks.get()
    g=grand_total.get()
    p=(t/g)*100
    if p>60:
        lbl.config(text="percentage is  "+str(p) ,bg="green",fg="white")
    else:
        lbl.config(text="percentage is  "+str(p),bg="red",fg="white")
    
total_marks=IntVar()
grand_total=IntVar()
Label(top,text="WELCOME TO PERCENTAGE CALCULATOR",bg="purple",fg="white",font=("arial",15,"bold")).grid(row=0,column=2,columnspan=2,pady=20)
Label(top,text="enter total marks").place(x=0,y=70)
Entry(top,textvariable=total_marks).place(x=100,y=70)
Label(top,text="%  of grand total").place(x=230,y=70)
Entry(top,textvariable=grand_total).place(x=350,y=70)
Button(top,text="calculate",command=calculate).place(x=50,y=150)
lbl=Label(top,font=("arial",15,"bold"))
lbl.place(x=50,y=200)
