from tkinter import *
top=Tk()
top.geometry("300x500")
top.configure(bg="red")
def tasks():
    task=e1.get()
    if task!=" ":
        Checkbutton(top,text=task,bg="aqua",fg="black").pack(pady=5)
        e1.set(" ")
e1=StringVar()
Label(top,text="TO-DO-LIST-APP",bg="#9d8189",fg="#370617",font=("arial",14,"bold")).pack(pady=5)
Label(top,text="enter the task you want to enter",bg="#b5838d",fg="black",font=("arial",12,"italic")).pack(pady=5)
Entry(top,textvariable=e1).pack(pady=5)
Button(top,text="add",command=tasks).pack(pady=5)
