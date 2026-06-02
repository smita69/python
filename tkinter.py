import tkinter as tk
top=tk.Tk()
top.geometry("300x500")
def add():
    a=num1.get()
    b=num2.get()
    result=mpty1.config(text="total is "+str(a+b))
def sub():
    a=num1.get()
    b=num2.get()
    result=mpty2.config(text="total is "+str(a-b))
def mul():
    a=num1.get()
    b=num2.get()
    result=mpty3.config(text="total is "+str(a*b))
def div():
    a=num1.get()
    b=num2.get()
    result=mpty4.config(text="total is "+str(a/b))

num1=tk.IntVar()
num2=tk.IntVar()


lbl1=tk.Label(top,text="small addition program",fg="green").place(x=50,y=50)
lbl2=tk.Label(top,text="1st number: ").place(x=30,y=120)
lbl3=tk.Label(top,text="2nd number: ").place(x=30,y=140)
ntry1=tk.Entry(top,textvariable=num1).place(x=200,y=120)
ntry2=tk.Entry(top,textvariable=num2).place(x=200,y=140)
btn=tk.Button(top,text="add",command=add).place(x=50,y=180)
btn=tk.Button(top,text="minus",command=sub).place(x=100,y=180)
btn=tk.Button(top,text="multiply",command=mul).place(x=150,y=180)
btn=tk.Button(top,text="devide",command=div).place(x=220,y=180)
mpty1=tk.Label(top)
mpty1.place(x=40,y=210)
mpty2=tk.Label(top)
mpty2.place(x=40,y=230)
mpty3=tk.Label(top)
mpty3.place(x=40,y=260)
mpty4=tk.Label(top)
mpty4.place(x=40,y=290)
