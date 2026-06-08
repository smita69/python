from tkinter import *
top=Tk()
top.geometry("300x500")
top.title("total fees calculation")
def calculate():
    total=0
    n=name.get()
    a=age.get()
    g=gender.get()
    if busfee.get()==1:
        total+=1100
    if tutionfee.get()==1:
        total+=1500
    if libraryfee.get()==1:
        total+=300
    if sportsfee.get()==1:
        total+=200
    if smartclassfee.get()==1:
        total+=3000
    if total>5000:
        t=total*0.5
        total-=t
        
    lbl1.config(text="name : " +str(n))
    lbl2.config(text="age : " +str(a))
    lbl3.config(text="gender : "+str(g))
    lbl4.config(text="total : " +str(total))
        
name=StringVar()
age=IntVar()
gender=StringVar(value=" ")
busfee=IntVar()
tutionfee=IntVar()
libraryfee=IntVar()
sportsfee=IntVar()
smartclassfee=IntVar()
Label(top,text="ABC SCHOOL JABALPUR",bg="red",fg="white").pack(pady=20)
Label(top,text="name").place(x=10,y=60)
Entry(top,textvariable=name).place(x=100,y=60)
Label(top,text="age").place(x=10,y=80)
Entry(top,textvariable=age).place(x=100,y=80)
Label(top,text="select gender").place(x=10,y=100)
Radiobutton(top,text="Male",variable=gender,value="male").place(x=10,y=120)
Radiobutton(top,text="Female",variable=gender,value="female").place(x=10,y=140)
Label(top,text="select fees that you have paid").place(x=10,y=160)
Checkbutton(top,text="bus fees(rs 1100)",variable=busfee).place(x=10,y=180)
Checkbutton(top,text="tution fees (rs 1500)",variable=tutionfee).place(x=10,y=200)
Checkbutton(top,text="library fees(rs 300)",variable=libraryfee).place(x=10,y=220)
Checkbutton(top,text="sports fees (rs 200)",variable=sportsfee).place(x=10,y=240)
Checkbutton(top,text="Smart class fees (rs 3000)",variable=smartclassfee).place(x=10,y=260)
Button(top,text="calculate" ,command=calculate,bg="coral",fg="white").place(x=50,y=290)
lbl1=Label(top)
lbl1.place(x=10,y=350)
lbl2=Label(top)
lbl2.place(x=10,y=370)
lbl3=Label(top)
lbl3.place(x=10,y=390)
lbl4=Label(top)
lbl4.place(x=10,y=410)
